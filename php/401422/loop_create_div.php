<?php

function colunaDiv($className, $primeiro, $ultimo) {
    echo '<div class="'.$className.'">';

    for($i = $primeiro; $i <= $ultimo; $i++) {
        echo '<div class="item">';
        echo $i;
        echo '</div>';
    }

    echo '</div>';
}

colunaDiv("coluna-1", 0, 4);
colunaDiv("coluna-2", 5, 6);

?>
