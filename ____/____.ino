int joystick_x;
int joystick_y;
int total_key;

void setup()
{
  Serial.begin(9600); //시리얼 통신을 하기위한 통신속도설정
  pinMode(A0, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
  pinMode(28, INPUT_PULLUP);
  pinMode(29, INPUT_PULLUP);
  pinMode(30, INPUT_PULLUP);
  pinMode(31, INPUT_PULLUP);
  pinMode(32, INPUT_PULLUP);
  pinMode(33, INPUT_PULLUP);
  pinMode(34, INPUT_PULLUP);
  pinMode(35, INPUT_PULLUP);
  pinMode(36, INPUT_PULLUP);
  pinMode(37, INPUT_PULLUP);
}

void loop()
{
  total_key = 1<<14;
  joystick_x = analogRead(A1); // X축 값이 표기됩니다.
  joystick_y = analogRead(A0); // X축 값이 표기됩니다.  
  if(joystick_x <= 350 and joystick_y >= 350 and joystick_y <= 650)
    total_key = total_key | 1<<13;   
  if(joystick_x >= 650 and joystick_y >= 350 and joystick_y <= 650)
    total_key = total_key | 1<<12;          
  if(joystick_y >= 650 and joystick_x >= 350 and joystick_x <= 650)
    total_key = total_key | 1<<11;              
  if(joystick_y <= 350 and joystick_x >= 350 and joystick_x <= 650)
    total_key = total_key | 1<<10;
  for(uint8_t i =0; i<10; i++){
    if(digitalRead(i+28) == LOW)
      total_key = total_key | 1<<9-i;
  }
  Serial.println(total_key,BIN);       
  delay(30);                      
}
