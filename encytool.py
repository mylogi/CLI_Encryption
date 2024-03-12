from classes.command_line_tool import CommandLineTool

if __name__ == "__main__":
    tool = CommandLineTool()
    state_tuple_data = tool.run()
    tool.input_loop()
    print(f"{tool.input_text=}")
    print(f"{tool.encrypt_or_decrypt(state_tuple_data)=}")
