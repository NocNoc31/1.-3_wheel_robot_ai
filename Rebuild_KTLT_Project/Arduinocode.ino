#include <Wire.h>
#include <SoftwareSerial.h>

SoftwareSerial HC06(1, 0); // Khai báo một đối tượng SoftwareSerial với chân TX trên Arduino là chân 1 và RX là chân 0
// Các chân điều khiển cho bánh xe trái và phải
const int leftWheel = 9; // Chân 9 trên Arduino điều khiển tốc độ của động cơ bánh xe trái
const int rightWheel = 3; // Chân 3 điều khiển tốc độ của động cơ bánh xe phải
const int in1 = 4; // in1 và in2 điều khiển hướng quay của động cơ bánh xe trái
const int in2 = 5;
const int in3 = 7; // in3 và in4 điều khiển hướng quay của động cơ bánh xe phải
const int in4 = 8;

int leftSpeed = 64; // Tốc độ ban đầu của động cơ bánh xe trái
int rightSpeed = 66; // Tốc độ ban đầu của động cơ bánh xe phải

void setup()
{
  // Serial.begin(38400); // Bỏ comment nếu bạn muốn sử dụng Serial Monitor
  HC06.begin(9600); // Khởi động kết nối với module Bluetooth HC-06
  // delay(20);
  pinMode(in1, OUTPUT); // Cấu hình các chân là OUTPUT để điều khiển động cơ
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(leftSpeed, OUTPUT);
  pinMode(rightSpeed, OUTPUT);
  delay(20); // Đợi 20ms
}

void loop()
{
  if (HC06.available()) // Nếu có dữ liệu từ module Bluetooth HC-06
  {
    char c = HC06.read(); // Đọc dữ liệu từ Bluetooth
    if (c == 'w')
    {
      forward(); // Điều khiển xe đi về phía trước
    }
    else if (c == 's')
    {
      reverse(); // Điều khiển xe đi lùi
    }
    else if (c == 'a')
    {
      turnLeft(); // Điều khiển xe rẽ trái
    }
    else if (c == 'd')
    {
      turnRight(); // Điều khiển xe rẽ phải
    }
    else if (c == '0')
    {
      stop(); // Dừng xe
    }
  }
}

void forward()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(rightWheel, rightSpeed);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(leftWheel, leftSpeed);
}

void reverse()
{
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(rightWheel, rightSpeed);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(leftWheel, leftSpeed);
}

void stop()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void turnLeft()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(rightWheel, rightSpeed);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(leftWheel, 0);
}

void turnRight()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(rightWheel, 0);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(leftWheel, leftSpeed);
}
