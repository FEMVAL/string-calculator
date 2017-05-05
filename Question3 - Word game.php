<?php 
        class Game {
        
        public $score;
 public $base;
        
        function __construct($base) { 
   }
        
        function submitWord($string_sub){
        
$arr = str_split($string_sub,1);
   print_r($arr);
$arr1 = str_split($base,1);
   foreach ($arr as $key => $value){
       
        foreach ($arr1 as $key => $value){
                
                }
      
      }


        
        }
        

        }

$obj = new Game("abcd");
$obj->submitWord('acd');

?>
