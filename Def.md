## Statements
Statement := (Assignment | While | Function | Return) ";"
Assignment := Variable "=" Expression
While := "while" "(" Expression ")" "{" [Statement]*"}"
Function := "def" Identifier "(" [Expression \[, Expression\]\*] ")" "{" Statement* "}"
Return := "return" Expression

## Expressions
Expression := Set | Operation | Variable
Set := "{"[Expression \[, Expression\]\*]*"}"
Function_Call := Identifier

### Operations
Operations := Union | Intersection | Difference | In | Equality
Union := Expression | Expression
Intersection := Expression & Expression
Difference := Expression - Expression
In := Expression "in" Expression
Equality := Expression "==" Expression

## Misc
Identifier := ([A..Z|a..z])*
