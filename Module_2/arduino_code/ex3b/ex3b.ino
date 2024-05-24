void setup() {
  delay(3000);
  Serial.begin(9600); // Iniciar a comunicação serial
}

void loop() {

  int n = 5;
  int list[3];
  int count = 0;
  for (int i = 1; i <= n; i++) {
    if (is_prime(i)) {
      list[count++] = i;
      Serial.write(i);
    }
  }
  
  int checksum = list[0] ^ list[1] ^ list[2];
  Serial.write(checksum);
}

// Função para verificar se um número é primo
bool is_prime(char n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
