<?php
  header("Content-type:text/xml");
  $feed = file_get_contents("https://www.gamespot.com/feeds/game-news/");
  echo $feed;
?>
