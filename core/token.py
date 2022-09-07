class Token:
    def __init__(self, token_type: str, lexeme: str, literal: str, line: None | int) -> None:
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        
    
    def scanner_result(self) -> str:
        [print(f'{self.token_type} | {self.lexeme} | {self.literal}') if self.line == None else print(f'{self.line} | {self.token_type} | {self.lexeme} | {self.literal}')]
