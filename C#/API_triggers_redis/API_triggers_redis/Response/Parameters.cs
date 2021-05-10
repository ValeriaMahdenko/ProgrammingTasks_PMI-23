using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API_triggers_redis.Response
{
	public class Parameters
	{

		private string _sort_by;
		private string _sort_type = "asc";
		private string _search;
		private int _offset;
		private int _limit;
		public string Sort_by
		{
			get => _sort_by;
			set { _sort_by = value; }
		}
		public string Sort_type
		{
			get => _sort_type;
			set { _sort_type = value; }
		}
		public string Search
		{
			get => _search;
			set { _search = value; }
		}
		public int Offset
		{
			get => _offset;
			set { _offset = value; }
		}
		public int Limit
		{
			get => _limit;
			set { _limit = value; }
		}
	}
}
