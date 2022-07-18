Compound_calc <- function(result){
  
  if(!any(colnames(result1) == c("parts", "mor"))){
    stop("not proper column name") 
  }
  
  result$id1 <- 1:nrow(result)
  result$id2 <- NA
  result$parts1 <- NA
  result$mor1 <- NA
  
  x <- 1
  for(n in 1:nrow(result)){
    #n <- 3
    a <- result[n,1] %in% c("名詞", "接頭詞", "接尾詞")
    if(a){
      if(n > 1){
        if(result[n-1,1] %in% c("名詞", "接頭詞", "接尾詞")){
          result[n,4] <- x
        }else{
          x <- x + 1
          result[n,4] <- x
        }
      }else{
        result[n,4] <- x
      }
    }else{
      x <- x + 1
      result[n,4] <- x
    }
  }
  
  #head(result)
  if(n == nrow(result)){
    for(m in 1:max(result$id2)){
      #m <- 18
      b <- result$mor[result$id2 == m]
      b1 <- paste0(b, collapse = "")
      d <- result$id1[result$id2 == m][1]
      
      if(length(b) == 1){
        result$parts1[d] <- result$parts[d]
        result$mor1[d] <- b1
      }else{
        result$parts1[d] <- "複合語"
        result$mor1[d] <- b1
      }
    }
  }
  
  result2 <- na.omit(result[,c("parts1", "mor1")])
  colnames(result2) <- c("parts", "mor")
  return(data.frame(result2, row.names = 1:nrow(result2)))
}