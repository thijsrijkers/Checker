<?php
    $jsonSource = "D:\!!!!!Checker\Storage\data.json";
    $data = "Word:"+$_POST["data"]+"";

    $array = array('WordsEntered' => $data);
    $fp = fopen($jsonSource, 'w');
    fwrite($fp, json_encode($array, JSON_PRETTY_PRINT)); 
    fclose($fp);
?>
