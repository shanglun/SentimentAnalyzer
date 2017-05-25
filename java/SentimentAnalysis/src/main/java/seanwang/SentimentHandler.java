package seanwang;

public class SentimentHandler implements SentimentAnalysisService.Iface {
    SentimentAnalyzer analyzer;
    SentimentHandler() {
        analyzer = new SentimentAnalyzer();
    }

    public String sentimentAnalyze(String sentence) {
        System.out.println("got: " + sentence);
        return analyzer.analyze(sentence);
    }

}
