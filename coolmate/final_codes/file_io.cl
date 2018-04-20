class Main
{
	(*a : String;
	b : String <- "file.txt";*)
	file_name : String <- "file.txt";
	input_str : String <- "extra";
	temp : String;
	def main : Int()
	{
		{
			(*out_string("Reading1\n");
			read_file(a, "large.txt");

			read_file(b,b);
			out_string(b);
			out_string(a);*)

			read_file(temp, file_name);

			concat_string(temp, input_str);
			
			write_file(file_name, temp);

			append_file(file_name, input_str);
		}

	};
};