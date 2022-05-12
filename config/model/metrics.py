


def scope_metrics(scope):
	metrics = { 
				'funds' : float,
				'donations' : float,
				'ada' : float,
				'apam' : float,
				'regos' : int,
				'active' : int,
				'regos_total_prior' : int,
				'regos_total_curnt' : int,
				'comment' : str,
	}

	scope.metrics = metrics