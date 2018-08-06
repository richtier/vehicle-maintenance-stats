
manage:
	DATABASE_URL=postgres://debug:debug@localhost:5432/vehicle_stats \
	./manage.py $(cmd)
