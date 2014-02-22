#include <iostream>

int days_in_month(int month, int year);
bool isLeapYear(int year);

int main()
{
	int day, month, year;

	int sundaysOnFirstOfTheMonth = 0;
	int weekday = 2; //Monday
	
	for (year = 1901; year <= 2000; year++)
	{
		for (month = 1; month <= 12; month++)
		{
			for (day = 1; day <= days_in_month(month, year); day++)
			{
				if (day == 1 and weekday == 0) sundaysOnFirstOfTheMonth++;
				weekday = (weekday + 1) % 7;
			}
		}
	}
	
	std::cout << sundaysOnFirstOfTheMonth;
	return 0;
}

int days_in_month(int month, int year)
{
	if (month==2 && isLeapYear(year)) return 29;

	switch (month)
	{
		case 2:
			return 28;
		case 4:
			return 30;
		case 6:
			return 30;
		case 9:
			return 30;
		case 11:
			return 30;
		default:
			return 31;
	}
}

bool isLeapYear(int year)
{
	if (year % 4 == 0 && (year % 400 == 0 || year % 100 != 0))
	{
		return true;
	}
	return false;
}
