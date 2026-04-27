class ChaiUtils:

  @staticmethod
  def clean_ingredients(text):
    return [item.strip() for item in text.split(",")]
  
#"water, milk   , ginger,  "

raw = "water, milk, ginger, honey"

#obj = ChaiUtils()
#obj.clean_ingredients(raw)



cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)