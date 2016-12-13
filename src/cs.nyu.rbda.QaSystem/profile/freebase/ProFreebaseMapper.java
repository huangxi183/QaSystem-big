
/**
 * Created by Huangxi on 11/12/2016.
 */
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class ProFreebaseMapper
        extends Mapper<LongWritable, Text, Text, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] temp = line.split(",");

        //Only take care of complete info in english
        if(temp.length == 8 ){
            //take subject as key, object + predicate as key
            context.write(new Text(temp[4].trim()), new Text(temp[6].trim()+","+temp[5].trim()));
            //take object as key, subject + predicate as key
            context.write(new Text(temp[6].trim()), new Text(temp[4].trim()+","+temp[5].trim()));
        }

    }
}

