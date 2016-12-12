#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
from SentenceClassifier import SentenceClassifier
from tensorflow.contrib import learn
import data_utils
import pickle

# ======================== MODEL HYPERPARAMETERS ========================================
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_integer("num_nodes", 16, "Number of nodes in fully connected layer")
tf.flags.DEFINE_float("learning_rate", 0.001, "Learning rate")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "Weight lambda on l2 regularization")

# Training Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size")
tf.flags.DEFINE_integer("num_epochs", 20, "Number of training epochs (default: 200)")
#tf.flags.DEFINE_integer("patience", 800, "Minimum number of batches seen before early stopping")
#tf.flags.DEFINE_integer("patience_increase", 6, "Number of dev evaluations of increasing loss before early stopping")

# Display/Saving Parameters
tf.flags.DEFINE_integer("evaluate_every", 50, "Evaluate model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", 50, "Save model after this many steps (default: 100)")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")
max_global_norm = 5

# Print
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")


# =============================== PREPARING DATA FOR TRAINING/VALIDATION/TESTING ===============================================
print("Loading data...")

context_dict = pickle.load(open("context_dict.p", "rb"))
question_dict = pickle.load(open("question_dict.p", "rb"))
answer_dict = pickle.load(open("answer_dict.p", "rb"))

dev_context_dict = pickle.load(open("dev_context_dict.p", "rb"))
dev_question_dict = pickle.load(open("dev_question_dict.p", "rb"))
dev_answer_dict = pickle.load(open("dev_answer_dict.p", "rb"))

embedding_matrix = np.load("embedding_matrix.npy")

# ================================================== MODEL TRAINING ======================================

with tf.Graph().as_default():
    session_conf = tf.ConfigProto(
        allow_soft_placement=FLAGS.allow_soft_placement,
        log_device_placement=FLAGS.log_device_placement)

    session_conf.gpu_options.allow_growth = True

    sess = tf.Session(config=session_conf)

    with sess.as_default():

        # FIX THISS
        sent_classifier = SentenceClassifier(embedding_matrix=embedding_matrix)
        #SentenceClassifer(hidden_size=10, vocab_size=42791, embedding_size=100, batch_size = FLAGS.batch_size)

        # optimizer = tf.train.GradientDescentOptimizer(0.000001)
        # global_step = tf.Variable(0, name='global_step', trainable=False)
        # trainables = tf.trainable_variables()
        # grads = tf.gradients(sent_classifier.loss, trainables)
        # grads, _ = tf.clip_by_global_norm(grads, clip_norm=max_global_norm)
        # grad_var_pairs = zip(grads, trainables)
        # print(grad_var_pairs)

        # capped_gvs = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gvs]
        #train_op = optimizer.apply_gradients(grad_var_pairs, global_step=global_step)
        #
        # # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(learning_rate = FLAGS.learning_rate)
        grads_and_vars = optimizer.compute_gradients(sent_classifier.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            # print("g, v")
            # print(g)
            # print(v)
            if g is not None:
                grad_hist_summary = tf.histogram_summary("{}/grad/hist".format(v.name), g)
                sparsity_summary = tf.scalar_summary("{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g))
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
            grad_summaries_merged = tf.merge_summary(grad_summaries)

        # Output directory for models and summaries
        timestamp = str(int(time.time()))
        out_dir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp))
        print("Writing to {}\n".format(out_dir))

        # Summaries for loss and accuracy
        loss_summary = tf.scalar_summary("loss", sent_classifier.loss)
        acc_summary = tf.scalar_summary("accuracy", sent_classifier.accuracy)

        # Train Summaries
        train_summary_op = tf.merge_summary([loss_summary, acc_summary, grad_summaries_merged])
        train_summary_dir = os.path.join(out_dir, "summaries", "train")
        train_summary_writer = tf.train.SummaryWriter(train_summary_dir, sess.graph)

        # Dev summaries
        dev_summary_op = tf.merge_summary([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
        dev_summary_writer = tf.train.SummaryWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        saver = tf.train.Saver(tf.all_variables())

        # Write vocabulary
        #all_corpus_vocabulary.save(os.path.join(out_dir, "vocab"))

        # Initialize all variables
        sess.run(tf.initialize_all_variables())


        def train_step(context, question, answer, verbose=False):

            #A single training step
            feed_dict = {
                sent_classifier.sentences : context,
                sent_classifier.questions : question,
                sent_classifier.labels : answer
            }

            #print ("Ready for training....")

            _, step, summaries, loss, accuracy, max_sent_per_doc, sentence_mask, probabilities, \
                question_cbow, cbow_sentences, masked_question_embeddings, \
                question_mask, masked_question, question_embeddings, masked_question_embeddings, W_embeddings = sess.run(
                [train_op, global_step, train_summary_op, sent_classifier.loss, sent_classifier.accuracy, sent_classifier.max_sent_per_doc, sent_classifier.sentence_mask, \
                    sent_classifier.probabilities, \
                    sent_classifier.question_cbow, sent_classifier.cbow_sentences, sent_classifier.masked_question_embeddings, sent_classifier.question_mask,\
                    sent_classifier.masked_question, sent_classifier.question_embeddings, sent_classifier.masked_question_embeddings, sent_classifier.W_embeddings],
                feed_dict)

            # _, step, summaries, loss, accuracy, max_sent_per_doc, sentence_mask, probabilities, masked_pos_cos_sim, cosine_similarity, \
            #     dot_prod, sentence_norm, question_norm, denom, question_cbow, cbow_sentences, masked_question_embeddings, \
            #     question_mask, masked_question, question_embeddings, masked_question_embeddings, W_embeddings = sess.run(
            #     [train_op, global_step, train_summary_op, sent_classifier.loss, sent_classifier.accuracy, sent_classifier.max_sent_per_doc, sent_classifier.sentence_mask, \
            #         sent_classifier.probabilities, sent_classifier.masked_pos_cos_sim, sent_classifier.cosine_similarity, \
            #         sent_classifier.dot_prod, sent_classifier.sentence_norm, sent_classifier.question_norm, sent_classifier.denom, \
            #         sent_classifier.question_cbow, sent_classifier.cbow_sentences, sent_classifier.masked_question_embeddings, sent_classifier.question_mask,\
            #         sent_classifier.masked_question, sent_classifier.question_embeddings, sent_classifier.masked_question_embeddings, sent_classifier.W_embeddings],
            #     feed_dict)

            time_str = datetime.datetime.now().isoformat()
            # print("\n\nNEW EXAMPLE")
            # print("W_embeddings")
            # print(W_embeddings)
            # print("sentence_mask")
            # print(sentence_mask)
            # print(max_sent_per_doc)
            # print("probabilities")
            # print(probabilities)
            # print("masked_pos_cos_sim")
            # print(masked_pos_cos_sim)
            # print("cosine_similarity")
            # print(cosine_similarity)
            # print("dot_prod")
            # print(dot_prod)
            # print("sentence_norm")
            # print(sentence_norm)
            # print("question_norm")
            # print(question_norm)
            # print("denom")
            # print(denom)
            # print("question_cbow")
            # print(question_cbow)
            # print("cbow_sentences")
            # print(cbow_sentences)
            # print("masked_question_embeddings")
            # print(masked_question_embeddings)
            # print("question_mask")
            # print(question_mask)
            # print("masked_question")
            # print(masked_question)
            # print("question_embeddings")
            # print(question_embeddings)
            # print("masked_question_embeddings")
            # print(masked_question_embeddings)
            # print("")
            # print()
            # print("")
            # print()
            # print("")
            # print()
            # print("")
            # print()
            # print("")
            # print()
            if verbose:
                print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))

            train_summary_writer.add_summary(summaries, step)

        def dev_step(context, question, answer, writer=None):

            # Evaluates model on a dev set
            feed_dict = {
                sent_classifier.sentences : context,
                sent_classifier.questions : question,
                sent_classifier.labels : answer
            }

            step, summaries, loss, accuracy = sess.run(
                [global_step, dev_summary_op, sent_classifier.loss, sent_classifier.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}\n\n".format(time_str, step, loss, accuracy))
            if writer:
                writer.add_summary(summaries, step)

        # Generate batches
        batches = data_utils.batch_iter(context_dict, question_dict, answer_dict, FLAGS.num_epochs, FLAGS.batch_size)

        count = 0
        for context, question, answer in batches:


            # print("context")
            # print(context)
            # print("question")
            # print(question)
            # print("answer")
            # print(answer)

            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                #10570
                batch_accuracy = train_step(context, question, answer, verbose=True)
                dev_batches = data_utils.batch_iter(dev_context_dict, dev_question_dict, dev_answer_dict, 1, 1000)
                print("\nEvaluation:")
                for dev_context, dev_question, dev_answer in dev_batches:
                    dev_step(dev_context, dev_question, dev_answer, writer=dev_summary_writer)
                    break
            else:
                batch_accuracy = train_step(context, question, answer)

            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))
