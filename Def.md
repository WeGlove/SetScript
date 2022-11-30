Statement := (Assignment) ";"

Assignment := Variable "=" Expression

Expression := Set | Operation | Variable

Set := "{"[Expression \[, Expression\]\*]*"}"

Operations := Union | Intersection | Difference | In

Union := Expression | Expression
Intersection := Expression & Expression
Difference := Expression - Expression
In := Expression "in" Expression
