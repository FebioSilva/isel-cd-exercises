void setup() {
  Serial.begin(9600); // Iniciar a comunicação serial
}

void loop() {
  int n = 100;
  for (int i = 1; i <= n; i++) {
    if (is_prime(i)) {
      Serial.write(i);
    }
  }
}

// Função para verificar se um número é primo
bool is_prime(int n) {
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