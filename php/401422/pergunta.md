Tenho o seguinte código php 

    for ($i = 0; $i <6; $i++){
        echo '<div class="item">';
        echo $i;
        echo '</div>';
        }
    ?>

Gostaria que as class até a posição 3 fossem envolvidas por uma div, e as duas classes restantes, fosse envolvidas por outra classe, para que o resultado final seja esse abaixo:

    <div class="coluna-1">
        <div class="item">0</div>
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
    </div>
    <div class="coluna-2">
        <div class="item">4</div>
        <div class="item">5</div>
    </div>

Fiz várias tentativas, mas não consegui, a forma que eu estava fazendo tava imprimindo um elemento dentro do outro.
