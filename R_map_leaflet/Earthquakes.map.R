if(!require("leaflet", quietly = TRUE)){
  install.packages("leaflet");require("leaflet")
}
if(!require("htmltools", quietly = TRUE)){
  install.packages("htmltools");require("htmltools")
}

library(leaflet)
library(htmltools)

Earthquakes.map <- function(Type=1){

  #URL定義
  csv_path <- "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
  
  #CSV読み込み
  Earthquakes <- read.table(file=csv_path, header = T, sep = ",")
  
  #地図の下準備
  #head(Earthquakes)
  Earthquakes <- Earthquakes[rev(order(Earthquakes$mag)),]
  map <- leaflet::leaflet(Earthquakes) %>% addTiles()
  
  #取得時間
  tim <- base::substr(Earthquakes[rev(order(Earthquakes$time)),][1,1], 
                      start=1, stop=16)
  title <- tags$p(tags$style("p {color: black; font-size:12px}"), tags$b(tim))
  
  ##ラベル作成
  Lab <- paste0("日時: ", Earthquakes$time, "<br>",
                "場所: ", Earthquakes$place, "<br>",
                "マグニチュード: ", Earthquakes$mag, "<br>",
                "深さ: ", Earthquakes$depth)
  
if(Type==1){

  #マーカーサイズ(1)
  size1 <- (2^Earthquakes$mag)*600
  
  #カラーパレット
  pal <- leaflet::colorNumeric(palette="Reds", domain=Earthquakes$mag)
  
  #地図作成: clusterOptions無し
  return(
  map %>% 
    addProviderTiles(providers$OpenMapSurfer) %>% 
    addCircles(lng=~longitude,lat=~latitude,
               radius=size1, color=~pal(Earthquakes$mag), weight=1, 
               stroke = TRUE, fillOpacity = 0.4, 
               popup = Lab,
               label =  ~as.character(mag),
               labelOptions = labelOptions(noHide = F, direction = 'center', textOnly = T)) %>% 
    addMiniMap(position="bottomright", width = 75, height = 75) %>% 
    addLegend(position='topright', pal=pal, values=~Earthquakes$mag, title="mag", opacity = 0.6) %>% 
    addControl(title, position = "bottomleft" )
  )
}else{
  if(Type==2){
  #マーカーサイズ(2)
  size2 <- (2^Earthquakes$mag)/2
  
  #地図作成: clusterOptions有り
  return(
  map %>% 
    addProviderTiles(providers$OpenMapSurfer) %>% 
    addCircleMarkers(lng=~longitude,lat=~latitude,
                     radius=size2, color="#09f", weight=1,
                     clusterOptions = markerClusterOptions(),
                     popup=Lab,
                     label =  ~as.character(mag),
                     labelOptions = labelOptions(noHide = T, direction = 'center', textOnly = T)
    ) %>% 
    addMiniMap(position="bottomright", width = 75, height = 75) %>% 
    addControl(title, position = "bottomleft" )
    )
  }else{
    
    #マーカーサイズ(1)
    size1 <- (2^Earthquakes$mag)*500
    
    #地図作成: clusterOptions無し
    return(
      map %>% 
        addProviderTiles(providers$OpenMapSurfer) %>% 
        addCircles(lng=~longitude,lat=~latitude,
                   radius=size1, color="#09f", weight=1, 
                   stroke = TRUE, fillOpacity = 0.4, 
                   popup = Lab,
                   label =  ~as.character(mag),
                   labelOptions = labelOptions(noHide = F, direction = 'center', textOnly = T)) %>% 
        addMiniMap(position="bottomright", width = 75, height = 75) %>% 
        addControl(title, position = "bottomleft" )
    )
  }}
  }




