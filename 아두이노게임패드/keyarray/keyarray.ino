#include <Keyboard.h>


void setup() {  
  Serial.begin(9600);
  Keyboard.begin();
  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);
  pinMode(A3, INPUT_PULLUP);
  pinMode(A4, INPUT_PULLUP);
  pinMode(A5, INPUT_PULLUP);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
}

void loop() {


  digitalWrite(2, LOW);
  if (digitalRead(A5)) Keyboard.release(96);
  else Keyboard.press(96);
  if (digitalRead(A4)) Keyboard.release(KEY_TAB);
  else Keyboard.press(KEY_TAB);
  if (digitalRead(A3)) Keyboard.release(KEY_CAPS_LOCK);
  else Keyboard.press(KEY_CAPS_LOCK);
  if (digitalRead(A2)) Keyboard.release(KEY_LEFT_SHIFT);
  else Keyboard.press(KEY_LEFT_SHIFT);
  if (digitalRead(A1)) Keyboard.release(KEY_LEFT_CTRL);
  else Keyboard.press(KEY_LEFT_CTRL);
  digitalWrite(2, HIGH);

  digitalWrite(3, LOW);
  if (digitalRead(A5)) Keyboard.release('1');
  else Keyboard.press('1');
  if (digitalRead(A4)) Keyboard.release('q');
  else Keyboard.press('q'); 
  if (digitalRead(A3)) Keyboard.release('a');
  else Keyboard.press('a');
  if (digitalRead(A2)) Keyboard.release('z');
  else Keyboard.press('z');
  if (digitalRead(A1)) Keyboard.release(KEY_LEFT_GUI);
  else Keyboard.press(KEY_LEFT_GUI);
  digitalWrite(3, HIGH);

    digitalWrite(4, LOW);
  if (digitalRead(A5)) Keyboard.release('2');
  else Keyboard.press('2');
  if (digitalRead(A4)) Keyboard.release('w');
  else Keyboard.press('w'); 
  if (digitalRead(A3)) Keyboard.release('s');
  else Keyboard.press('s');
  if (digitalRead(A2)) Keyboard.release('x');
  else Keyboard.press('x');
  if (digitalRead(A1)) Keyboard.release(KEY_LEFT_ALT);
  else Keyboard.press(KEY_LEFT_ALT);
  digitalWrite(4, HIGH);

  digitalWrite(5, LOW);
  if (digitalRead(A5)) Keyboard.release('3');
  else Keyboard.press('3');
  if (digitalRead(A4)) Keyboard.release('e');
  else Keyboard.press('e'); 
  if (digitalRead(A3)) Keyboard.release('d');
  else Keyboard.press('d');
  if (digitalRead(A2)) Keyboard.release('c');
  else Keyboard.press('c');
  digitalWrite(5, HIGH);

  digitalWrite(6, LOW);
  if (digitalRead(A5)) Keyboard.release('4');
  else Keyboard.press('4');
  if (digitalRead(A4)) Keyboard.release('r');
  else Keyboard.press('r'); 
  if (digitalRead(A3)) Keyboard.release('f');
  else Keyboard.press('f');
  if (digitalRead(A2)) Keyboard.release('v');
  else Keyboard.press('v');
  digitalWrite(6, HIGH);

    digitalWrite(7, LOW);
  if (digitalRead(A5)) Keyboard.release('5');
  else Keyboard.press('5');
  if (digitalRead(A4)) Keyboard.release('t');
  else Keyboard.press('t'); 
  if (digitalRead(A3)) Keyboard.release('g');
  else Keyboard.press('g');
  if (digitalRead(A2)) Keyboard.release('b');
  else Keyboard.press('b');
  digitalWrite(7, HIGH);

    digitalWrite(8, LOW);
  if (digitalRead(A5)) Keyboard.release('6');
  else Keyboard.press('6');
  if (digitalRead(A4)) Keyboard.release('y');
  else Keyboard.press('y'); 
  if (digitalRead(A3)) Keyboard.release('h');
  else Keyboard.press('h');
  if (digitalRead(A2)) Keyboard.release('n');
  else Keyboard.press('n');
  digitalWrite(8, HIGH);

  digitalWrite(9, LOW);
  if (digitalRead(A5)) Keyboard.release('7');
  else Keyboard.press('7');
  if (digitalRead(A4)) Keyboard.release('u');
  else Keyboard.press('u'); 
  if (digitalRead(A3)) Keyboard.release('j');
  else Keyboard.press('j');
  if (digitalRead(A2)) Keyboard.release('m');
  else Keyboard.press('m');
    if (digitalRead(A1)) Keyboard.release(32);
  else Keyboard.press(32);
  digitalWrite(9, HIGH);
  
  digitalWrite(10, LOW);
  if (digitalRead(A5)) Keyboard.release('8');
  else Keyboard.press('8');
  if (digitalRead(A4)) Keyboard.release('i');
  else Keyboard.press('i'); 
  if (digitalRead(A3)) Keyboard.release('k');
  else Keyboard.press('k');
  digitalWrite(10, HIGH);

  digitalWrite(11, LOW);
  if (digitalRead(A5)) Keyboard.release('9');
  else Keyboard.press('9');
  if (digitalRead(A4)) Keyboard.release('o');
  else Keyboard.press('o'); 
  if (digitalRead(A3)) Keyboard.release('l');
  else Keyboard.press('l');
  if (digitalRead(A2)) Keyboard.release(44);
  else Keyboard.press(44);
  if (digitalRead(A1)) Keyboard.release(KEY_RIGHT_ALT);
  else Keyboard.press(KEY_RIGHT_ALT);
  digitalWrite(11, HIGH);

  digitalWrite(12, LOW);
  if (digitalRead(A5)) Keyboard.release('0');
  else Keyboard.press('0');
  if (digitalRead(A4)) Keyboard.release('p');
  else Keyboard.press('p'); 
  if (digitalRead(A3)) Keyboard.release(59);
  else Keyboard.press(59);
  if (digitalRead(A2)) Keyboard.release(46);
  else Keyboard.press(46);
  if (digitalRead(A1)) Keyboard.release(KEY_RIGHT_GUI);
  else Keyboard.press(KEY_RIGHT_GUI);
  digitalWrite(12, HIGH);

  digitalWrite(13, LOW);
  if (digitalRead(A5)) Keyboard.release(45);
  else Keyboard.press(45);
  if (digitalRead(A4)) Keyboard.release(91);
  else Keyboard.press(91); 
  if (digitalRead(A3)) Keyboard.release(39);
  else Keyboard.press(39);
  if (digitalRead(A2)) Keyboard.release(47);
  else Keyboard.press(47);
  if (digitalRead(A1)) Keyboard.release(254);
  else Keyboard.press(254);
  digitalWrite(13, HIGH);

  digitalWrite(14, LOW);
  if (digitalRead(A5)) Keyboard.release(61);
  else Keyboard.press(61);
  if (digitalRead(A4)) Keyboard.release(93);
  else Keyboard.press(93); 
  digitalWrite(14, HIGH);

  digitalWrite(15, LOW);
  if (digitalRead(A5)) Keyboard.release(KEY_BACKSPACE);
  else Keyboard.press(KEY_BACKSPACE);
  if (digitalRead(A4)) Keyboard.release(92);
  else Keyboard.press(92); 
  if (digitalRead(A3)) Keyboard.release(KEY_RETURN);
  else Keyboard.press(KEY_RETURN);
  if (digitalRead(A2)) Keyboard.release(KEY_RIGHT_SHIFT);
  else Keyboard.press(KEY_RIGHT_SHIFT);
  if (digitalRead(A1)) Keyboard.release(KEY_RIGHT_CTRL);
  else Keyboard.press(KEY_RIGHT_CTRL);
  digitalWrite(15, HIGH);
}
