package seanwang;

/**
 * Created by shang on 5/17/2017.
 */
public class SentimentHandler implements SentimentAnalysisService.Iface {

    public String sentimentAnalyze(String sentence) {
        System.out.println("got: " + sentence);
        return "Hello";
    }

}
