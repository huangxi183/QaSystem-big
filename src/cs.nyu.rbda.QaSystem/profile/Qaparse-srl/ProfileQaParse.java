/**
 * Created by Huangxi on 11/11/2016.
 */
//package QaParse;
import java.io.*;

public class ProfileQaParse {
    public static void main(String[] args) throws IOException{
        File resultfile = new File("src/output.txt");
        File file = new File("src/input.txt");
        BufferedReader reader = null;
        try {
            String tempString = null;
            reader = new BufferedReader(new FileReader(file));
            FileWriter fWriter = new FileWriter(resultfile);
            while ((tempString = reader.readLine()) != null) {
                String[] temp = tempString.split("\t");
                int i = Integer.valueOf(temp[1]);
                fWriter.write(temp[0]+"|");
                tempString = reader.readLine();
                fWriter.write(tempString+"|");
                while(i != 0){
                    tempString = reader.readLine();
                    String[] temp1 = tempString.split("\t");
                    for(int r = Integer.valueOf(temp1[2]); r > 0 ; r --){
                        tempString = reader.readLine();
                        fWriter.write(tempString+"|");
                    }
                    i--;
                }
                tempString = reader.readLine();
                fWriter.write("\n");
            }
            fWriter.close();
            reader.close();
        }
         catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                }
            }
        }
    }
}
