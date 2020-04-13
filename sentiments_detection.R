library("rjson")
library("tibble")
library("stringr")
library("dplyr")
library("jsonlite")
library(tidytext)
library(reshape2)
library(textdata)
library(wordcloud)
library(RColorBrewer)
install.packages("webshot")


my_table <- read_json("./final.json", simplifyVector = TRUE)
                   
tweet_words = my_table %>%
  select(text,
         hashtags,
         sentiment_indicator) %>%
  unnest_tokens(word, text)



nrc_words <- get_sentiments("nrc")
bing = get_sentiments("bing")

tweet_words %>%
  count(word) %>%
  with(wordcloud(word, n, max.words = 100, random.order = FALSE,scale=c(4,0.7), 
                 colors=brewer.pal(8, "Dark2"),random.color = TRUE))

tweet_words %>%
  inner_join(nrc_words, by = c("word" = "word")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = brewer.pal(2, "Dark2"),
                   max.words = 200)


nrc_words <- tweet_words %>%
  inner_join(nrc_words, by = "word")


sentiments_rank <- nrc_words %>%
  group_by(sentiment) %>%
  tally %>%
  arrange(desc(n))


