class Main
{
	(*a : String;
	b : String <- "file.txt";*)
	file_name : String <- "file.txt";
	input_str : String <- "Now I am complete";
	def main : Int()
	{
		{
			(*out_string("Reading1\n");
			read_file(a, "large.txt");

			read_file(b,b);
			out_string(b);
			out_string(a);*)

			write_file(file_name, input_str);
		}

	};
};