import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MaxMinContext {
        public static void main(String args[]) throws Exception {
                if (args.length != 2) {
                        System.err.println("Usage: MaxMinContext <input path> <output path>");
                        System.exit(-1);
                }

                Job job = new Job();
                job.setJarByClass(MaxMinContext.class);
                job.setJobName("Count max and min length of context");

                FileInputFormat.addInputPath(job, new Path(args[0]));
                FileOutputFormat.setOutputPath(job, new Path(args[1]));

                job.setMapperClass(MaxMinContextMapper.class);
                job.setReducerClass(MaxMinContextReducer.class);

                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(IntWritable.class);

                System.exit(job.waitForCompletion(true) ? 0 : 1);
        }
}