import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MaxMinContextReducer extends Reducer<Text, IntWritable, IntWritable, IntWritable> {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
                int max = Integer.MIN_VALUE;
                int min = Integer.MAX_VALUE;
                for (IntWritable value : values) {
                        int length = value.get();
                        if (length == 0)
                                continue;
                        max = Math.max(max, length);
                        min = Math.min(min, length);
                }
                context.write(new IntWritable(max), new IntWritable(min));
        }
}