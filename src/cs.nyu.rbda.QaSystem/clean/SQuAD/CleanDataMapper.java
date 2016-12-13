import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanDataMapper extends Mapper<LongWritable, Text, Text, Text> {
        @Override
        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
                String text = value.toString();
                int length = text.length();
                // onlt those text with length between 50-200 would be selected
                if (length <= 200 && length >= 50) {
                	context.write(new Text(text), new Text(text));	
                }
        }
}
