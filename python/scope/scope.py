# Global Scope
global_var = "I'm a global variable"

def outer_function():
    # Enclosing Scope
    outer_var = "I'm an outer variable"
    
    def inner_function():
        # Local Scope
        local_var = "I'm a local variable"
        print(local_var)
        print(outer_var)
        print(global_var)
    
    inner_function()

outer_function()
print(global_var)
