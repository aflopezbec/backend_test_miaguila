function generate(x) {
   var array =  new Array(x);

   function printIndex(index){
       return function(){
           return index;
       }
   }
   
   for(var i=0; i<array.length; i++){
       array[i] = printIndex(i);
   }
   return array;
}

var a = generate(5);
console.log(a[0]());
console.log(a[1]());