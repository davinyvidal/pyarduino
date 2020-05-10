int led1 = 13; // Porta onde o led será inserido


void setup(){
  Serial.begin(9600); // Velocidade padrão do Uno
  pinMode(led1, OUTPUT); // Porta onde o led será inserido, configurado como saida
}
void loop(){
  char leitura = Serial.read(); // Variavel que receberá os valores enviados pelo programa em python
  if(leitura == '1'){
    digitalWrite(led1, HIGH); // Liga a porta 13 se o valor recebido for 1
  }
  else if(leitura == '2'){
    digitalWrite(led1, LOW); // Desliga a porta 13 se o valor recebido for 2
  }
}