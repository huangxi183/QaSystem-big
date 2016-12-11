import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class QuestionTypeMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{
		String[] words = new String[]{"what","which","who","where","when","if"};
		String question = value.toString().toLowerCase();
		for (String word : words) {
			if (question.matches("(.*)" + word + "(.*)")) {
				context.write(new Text(word), new IntWritable(1));
			}
			else {
				context.write(new Text(word), new IntWritable(0));
			}
		}
	}
}