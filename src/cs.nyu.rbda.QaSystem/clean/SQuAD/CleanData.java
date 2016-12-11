import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CleanData {
        public static void main(String args[]) throws Exception {
                if (args.length != 2) {
                        System.err.println("Usage: CleanData <input path> <output path>");
                        System.exit(-1);
                }

                Job job = new Job();
                job.setJarByClass(CleanData.class);
                job.setJobName("Clean Data : select the text whose length is between 50 and 200");

                FileInputFormat.addInputPath(job, new Path(args[0]));
                FileOutputFormat.setOutputPath(job, new Path(args[1]));

                job.setMapperClass(CleanDataMapper.class);
                job.setReducerClass(CleanDataReducer.class);

                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(Text.class);

                System.exit(job.waitForCompletion(true) ? 0 : 1);
        }
}