# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.
def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ava = set(supplies)
        
        intor = {}
        
        indegree = {}
        
        rtoi = {}
        
        for i, recipe in enumerate(recipes):
            recipe_ingredients = ingredients[i]
            rtoi[recipe] = recipe_ingredients
            indegree[recipe] = len(recipe_ingredients)
            
            for ingredient in recipe_ingredients:
                if ingredient not in intor:
                    intor[ingredient] = []
                intor[ingredient].append(recipe)
        
        queue = list(ava)
        res = []
        
        while queue:
            current = queue.pop(0)
            
            if current in rtoi:
                res.append(current)
            
            if current in intor:
                for dependent_recipe in intor[current]:
                    indegree[dependent_recipe] -= 1
                    
                    if indegree[dependent_recipe] == 0:
                        queue.append(dependent_recipe)
        
        return res