#include<stdio.h>
int royal_flush();
int straight_flush();
int four_of_a_kind();
int full_house();
int flush();
int straight();
int three_of_a_kind();
int two_pairs();
int pair();

char ranks[] = {'K','Q','J','T','9','8','7','6','5','4','3','2','A'};
char hands[5][2];

int main()
{
  int len;
  int count;
  scanf("%d", &count);
  char ch;
  while(count--)
    {
      len = 4;
      while(len >= 0)
	{
	  do
	    {     
	      scanf("%c", &ch);
	    }while(ch == '\n' || ch == ' ' || ch == '	');
	  hands[len][0] = ch;
     
	  do
	    {
	      scanf("%c", &ch);
	    }while(ch == '\n' || ch == ' ' || ch == '	');
	  hands[len][1] = ch;
	  len--;
	}
      if(royal_flush()){printf("royal flush");}
      else if(straight_flush()){printf("straight flush");}
      else if(four_of_a_kind()){printf("four of a kind");}
      else if(full_house()){printf("full house");}
      else if(flush()){printf("flush");}
      else if(straight()){printf("straight");}
      else if(three_of_a_kind()){printf("three of a kind");}
      else if(two_pairs()){printf("two pairs");}
      else if(pair()){printf("pair");}
      else{printf("high card");}
   
      printf("\n");
    }
   
  return 0;
}

int royal_flush()
{
  char type = hands[0][1];
  int ret = 1;
  int i;
  for(i=0; i<5; i++)
    {
      if(hands[i][1] != type || hands[i][0] != 'A' &&
	 hands[i][0] != 'K' &&
	 hands[i][0] != 'Q' &&
	 hands[i][0] != 'J' &&
	 hands[i][0] != 'T')
	{
	  ret = 0;
	  break;
	} 
    }
  return ret;
}
int straight_flush()
{
  char type = hands[0][1];
  int i = 0;
  int j = 0;
  char ch;
  int min = 12;
  int max = 0;
  int ret = 1;
  while(i < 5)
    {
      if(hands[i][1] != type)
	{
	  ret = 0;
	  break;
	} 
      for(j=0; j<=12; j++)
	{
	  if(ranks[j] == hands[i][0])
	    {
	      if(min > j) min = j;
	      if(max < j) max = j;
	      break;
	    }
	}
      i++;
    }
  if(ret)
    ret = (max - min) == 4 ? 1 : 0;
  return ret;
}
int four_of_a_kind()
{
  int i = 0;
  int c1, c2;
  c1 = c2 = 0;
  for(i=0; i<5; i++)
    {
      if(hands[i][0] == hands[0][0]) c1++;
      if(hands[i][0] == hands[1][0]) c2++;
    }
  return c1 == 4 || c2 == 4 ? 1 : 0;
}
int full_house()
{
  int i = 0;
  int c1, c2;
  c1 = c2 = 0;
  char *p1, *p2;
  p1 = &hands[i][0];
  for(i=0; i<5; i++)
    {
      if(hands[i][0] == *p1) c1++;
      else
	{
	  if(!c2)
	    {
	      p2 = &hands[i][0];
	      c2++;
	    }
	  else if(hands[i][0] == *p2)
	    {
	      c2++;
	    }     
	  else return 0;
	} 
    }
  return 1;

}
int flush()
{
  int i = 0;
  char type = hands[0][1];
  while(i<5)
    {
      if(hands[i][1] != type)
	return 0;
      i++;
    }
  return 1;
}
int straight()
{
  int i = 0;
  int j = 0;
  
  int ret = 1;
  int ace = 0;
  char list[13];
  for(i=0; i<13; i++)
    list[i] = '\0';
  i=0;
  while(i < 5)
    {
      for(j=0; j<=12; j++)
	{
	  if(ranks[j] == hands[i][0])
	    {
	      if(j==12)
		{
		  if(ace == 0)
		    ace = 1;
		  else
		    return 0;
		}
	      else 
		{
		  if(list[j] == '\0')    
		    list[j] = 'x';
		  else
		    return 0;
		}
	    }
	}
      i++;
    }

  i=0;
  for(j=0; j<=12; j++)
    {
      if(list[j] == 'x')
	{
	  if(j==0 || list[j-1] == '\0')
	    i=0;
	  i++;
	}
    }

  if(i==4 && (list[0] == 'x' || list[11] == 'x'))  i++;
    
  
  return i==5?1:0;
}
int three_of_a_kind()
{
  int i = 0;
  int c1, c2, c3;
  c1 = c2 = c3 = 0;
  char *p1, *p2, *p3;
  p1 = &hands[i][0];
  for(i=0; i<5; i++)
    {
      if(hands[i][0] == *p1) c1++;
      else if(!c2)
	{
	  p2 = &hands[i][0];
	  c2++;
	}
      else if(hands[i][0] == *p2) c2++;
      else if(!c3)
	{
	  p3 = &hands[i][0];
	  c3++;
	}
      else if(hands[i][0] == *p3)
	{
	  c3++;
	}     
    }
  return c1 == 3 || c2 == 3 || c3 == 3 ? 1 : 0;
}
int two_pairs()
{
  int i = 0;
  int c1, c2, c3;
  c1 = c2 = c3 = 0;
  char *p1, *p2, *p3;
  p1 = &hands[i][0];
  for(i=0; i<5; i++)
    {
      if(hands[i][0] == *p1) c1++;
      else if(!c2)
	{
	  p2 = &hands[i][0];
	  c2++;
	}
      else if(hands[i][0] == *p2) c2++;
      else if(!c3)
	{
	  p3 = &hands[i][0];
	  c3++;
	}
      else if(hands[i][0] == *p3)
	{
	  c3++;
	}     
    }
  return c1 == 2 && c2 == 2 || c1 == 2 && c3 == 2  || c2 == 2 && c3 == 2 ? 1 : 0;
}
int pair()
{
  int i = 0;
  int c1, c2, c3,c4;
  c1 = c2 = c3 = c4 = 0;
  char *p1, *p2, *p3, *p4;
  p1 = &hands[0][0];
  for(i=0; i<5; i++)
    {
      if(hands[i][0] == *p1) c1++;
      else if(!c2)
	{
	  p2 = &hands[i][0];
	  c2++;
	}
      else if(hands[i][0] == *p2) c2++;
      else if(!c3)
	{
	  p3 = &hands[i][0];
	  c3++;
	}
      else if(hands[i][0] == *p3)
	{
	  c3++;
	}  
      else if(!c4)
	{
	  p4 = &hands[i][0];
	  c4++;
	}
      else if(hands[i][0] == *p4)
	{
	  c4++;
	}   
    }
  return c1 == 2 || c2 == 2 || c3 == 2 || c4 == 2 ? 1 : 0;
}
