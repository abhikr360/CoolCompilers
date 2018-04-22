class Main
{
	(*a : String;
	b : String <- "file.txt";*)
	file_name : String <- "file.txt";
	input_str : String <- "extra";
	append_string : String <- "append";
	temp : String;
	def main : Int()
	{
		{

			read_file(temp, file_name);
			
			out_string("Original content of file\n");
			out_string(temp);

			concat_string(temp, input_str);

			out_string("\nconcat_string result : \n");
			out_string(temp);

			
			write_file(file_name, temp);

			out_string("\nwritten content of file\n");
			out_string(temp);


			append_file(file_name, append_string);
		}

	};
};