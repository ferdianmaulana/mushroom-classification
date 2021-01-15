def findDecision(obj): #obj[0]: cap-shape, obj[1]: cap-surface, obj[2]: cap-color, obj[3]: bruises, obj[4]: odor, obj[5]: gill-attachment, obj[6]: gill-spacing, obj[7]: gill-size, obj[8]: gill-color, obj[9]: stalk-shape, obj[10]: stalk-root, obj[11]: stalk-surface-above-ring, obj[12]: stalk-surface-below-ring, obj[13]: stalk-color-above-ring, obj[14]: stalk-color-below-ring, obj[15]: veil-type, obj[16]: veil-color, obj[17]: ring-number, obj[18]: ring-type, obj[19]: spore-print-color, obj[20]: population, obj[21]: habitat
   if obj[4] == 'n':
      if obj[16] == 'w':
         if obj[17] == 'o':
            if obj[7] == 'b':
               return 'e'
            elif obj[7] == 'n':
               if obj[3] == 'f':
                  return 'e'
               elif obj[3] == 't':
                  return 'p'
               else:
                  return 'p'
            else:
               return 'e'
         elif obj[17] == 't':
            if obj[19] == 'r':
               return 'p'
            elif obj[19] == 'w':
               return 'e'
            else:
               return 'e'
         else:
            return 'p'
      elif obj[16] == 'y':
         return 'p'
      else:
         return 'p'
   elif obj[4] == 'f':
      return 'p'
   elif obj[4] == 'a':
      return 'e'
   elif obj[4] == 'l':
      return 'e'
   elif obj[4] == 'p':
      return 'p'
   elif obj[4] == 'c':
      return 'p'
   elif obj[4] == 'm':
      return 'p'
   else:
      return 'p'
