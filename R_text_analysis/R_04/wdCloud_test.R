#複合語抽出: Compound_calc()関数を使います
source("https://raw.githubusercontent.com/kumeS/Blog/master/R_text_analysis/R_03/Compound_calc.R")

wdCloud.R <- function(result, parts=c("名詞", "複合語", Top=9)){

#実行
result1c <- Compound_calc(result = result)

#品詞から「名詞」と「形容詞」と「動詞」を抽出
result2 <- result1c[result1c$parts %in% parts,]

#品詞の集計
cat("result2")
print(table(result2$parts))
#複合語   名詞 
#   137   1003

#平仮名1文字の形態素を除く
result3 <- result2[!base::grepl(pattern="^[あ-ん]$", result2$mor),]

#品詞の集計
cat("result3")
print(table(result3$parts))
#複合語   名詞 
#   137    972

#集計
Dat <- data.frame(mor=names(table(result3$mor)),
                  Freq=as.numeric(table(result3$mor)))

#頻度1回を除く
Dat <- Dat[Dat$Freq != 1,]

#形態素頻度を0~1の値に補正
Dat$FreqR <- round(Dat$Freq/max(Dat$Freq), 4)

#出現数上位20%のみ抽出
res <- quantile(Dat$FreqR, probs = seq(0, 1, 0.1))
Dat0 <- Dat[Dat$FreqR > as.numeric(res[Top]),]

#抽出の結果
cat("Dat0")
cat(dim(Dat0))
#[1] 30  3

#表示
print(head(Dat0[order(Dat0$Freq, decreasing = T),]))

#wordcloud2.jsによるワードクラウド作成
Dat1 <- wordcloud2(Dat0[,c("mor", "FreqR")],
                   shape="circle",
                   size=0.8,
                   gridSize =  1,
                   fontFamily="YuGothic",
                   color = "random-light",
                   ellipticity = 0.75,
                   backgroundColor = "black")

return(Dat1)
}






