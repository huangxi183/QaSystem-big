package cs.nyu.edu.snlp.qasystem.utils;

import cs.nyu.edu.snlp.qasystem.Answer;
import cs.nyu.edu.snlp.qasystem.DataSet;
import cs.nyu.edu.snlp.qasystem.Datum;
import cs.nyu.edu.snlp.qasystem.QA;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.List;


public class Test {
    public static void main(String args[]) throws IOException{
        DataSet dataSet = DataSet.loadFromFile("dev-v1.1.json");
        List<Datum> data = dataSet.getData();
        for (Datum dat : data) {
            String context = dat.getContext();
            System.out.println("context: " + context.substring(0,10));
            List<QA> qas = dat.getQas();
            for (QA qa : qas) {
                String id = qa.getId();
                String question = qa.getQuestion();
                System.out.println("id: " + id);
                System.out.println("question: " + question);
                List<Answer> answers = qa.getAnswers();
                System.out.println("answers: ");
                for (Answer answer : answers) {
                    String text = answer.getText();
                    System.out.println(text);
                }
            }
            System.out.println("=======================");
        }

    }
}
