import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
public class MaxLengthMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] temp = line.split("|");
        //String[] wiki = temp[0].split("_");
        //context.write(new Text("wiki"), new IntWritable(Integer.valueOf(wiki[1])) );
        int l = temp.length;
        l = l - 2;
        context.write(new Text("sentence"), new IntWritable(temp[1].length() ));
        int maxl = 0;
        for(int i = 0; i < l - 1; i ++){
            if(maxl < temp[2+i].length())
                maxl = temp[2+i].length();
        }
        context.write(new Text("questionanswer"), new IntWritable(maxl));
    }
}
