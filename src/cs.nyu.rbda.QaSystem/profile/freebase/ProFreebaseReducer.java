
/**
 * Created by Huangxi on 11/12/2016.
 */
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
public class ProFreebaseReducer extends Reducer<Text, Text, Text, Text>{
    @Override
    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        StringBuilder sb = new StringBuilder();

        for (Text value : values) {
            sb.append(value.toString());
            sb.append(",");
        }
        context.write(key, new Text(sb.toString()));

    }
}


