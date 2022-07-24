def add_time(start_time, duration, starting_date = None):

  v_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]  
  v_day=""
  v_temp=start_time.split()
  v_start_time=v_temp[0].split(":")
  v_start_time.append(v_temp[1])
  v_hora_final=0
  v_AMPM =""
  v_next_day=""
  v_temp=duration.split(":")
  k=0

  v_minutos_final=int(v_start_time[1])+int(v_temp[1])

  if v_minutos_final>=60:
    v_hora_final=int(int(v_minutos_final)/60)+int(v_temp[0])+int(v_start_time[0])
    if (v_minutos_final-60) ==0:
      v_minutos_final="00"
    elif len(str(v_minutos_final-60))<2:
      v_minutos_final="0"+ str(v_minutos_final-60)
    else:
      v_minutos_final=str(v_minutos_final-60)
    
  else:
    v_hora_final = v_hora_final + int(v_start_time[0]) + int(v_temp[0])
  if v_start_time[2] == "PM":
      v_hora_final = v_hora_final + 12


  i = int(v_hora_final/24)
  
  #print (v_hora_final)
  v_hora_final = v_hora_final - (i*24)
  if v_hora_final == 0:
    v_hora_final=12
  
  if v_hora_final<12:
    v_AMPM="AM"
  else:
    if v_hora_final>12:
      v_hora_final=v_hora_final-12
    v_AMPM="PM"

  if i >= 1 and i <2:
    v_next_day="(next day)"

  elif i > 1:
    v_next_day="("+str(i)+" days later)"

  if starting_date == None:
    print("# Returns: "+str(v_hora_final)+":"+str(v_minutos_final)+" "+v_AMPM+ " " + v_next_day)
  else:
    l=0
    for day in v_days:  ##################################################
      l+=1
      
      if starting_date.upper() == day.upper():
       break
      
    print(f"# Returns: "+str(v_hora_final)+":"+str(v_minutos_final)+" "+v_AMPM+ f", {v_days[l-1+i]} " + v_next_day)
