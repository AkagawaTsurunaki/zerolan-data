from dataclasses import dataclass


@dataclass
class ICIOPrompt:
    """
    Instruction: The specific task you want the model to perform.

    Context (optional): Contextual information, or contextual information, which helps guide the model to react more accurately.

    Input Data (optional): Tells the model the specific data that needs to be processed.

    Output Indicator (optional): Output Indicator: Indicates the type or format we expect the model to output.
    """
    instruction: str | None = None
    context: str | None = None
    input_data: str | None = None
    output_indicator: str | None = None

    def en_format(self):
        result = ""
        result += f"Instruction: {self.instruction}\n" if self.instruction is not None else ""
        result += f"Context: {self.context}\n" if self.context is not None else ""
        result += f"Input: {self.input_data}\n" if self.input_data is not None else ""
        result += f"Indicator: {self.output_indicator}" if self.output_indicator is not None else ""
        return result
