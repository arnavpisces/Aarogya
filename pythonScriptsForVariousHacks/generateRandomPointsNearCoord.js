var i;
for (i=0;i<10;i++){
  var r = 2500/111300 // = 1000 meters

  , y0 = 28.635901
  
  , x0 = 77.201854
  
  , u = Math.random()
  
  , v = Math.random()
  
  , w = r * Math.sqrt(u)
  
  , t = 2 * Math.PI * v
  
  , x = w * Math.cos(t)
  
  , y1 = w * Math.sin(t)
  
  , x1 = x / Math.cos(y0)
  
  
  newY = y0 + y1
  
  newX = x0 + x1
  console.log(newX+','+newY)

// console.log(newX)
}



