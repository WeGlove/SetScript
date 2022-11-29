Statement := (Assignment) ";"

Assignment := Variable "=" Expression

Expression := Set | Operation | Variable

Set := "{""}"

Operations := Union | Intersection | without

Union := Expression + Expression
Intersection := Expression * Expression
without := Expression / Expression
