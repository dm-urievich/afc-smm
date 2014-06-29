LIBRARY ieee;
USE ieee.std_logic_1164.all;
use IEEE.STD_LOGIC_arith.all;
use IEEE.STD_LOGIC_signed.all;

--  Entity Declaration
ENTITY pid_controller IS
	PORT
	(
        CLK     : IN STD_LOGIC;
        en 		 : IN STD_LOGIC;
        init    : IN STD_LOGIC;

		  error   : IN STD_LOGIC_VECTOR(15 downto 0);
		  
        init_val : IN STD_LOGIC_VECTOR(15 downto 0);
        kp	    : IN STD_LOGIC_VECTOR(15 downto 0);
        ki      : IN STD_LOGIC_VECTOR(15 downto 0);

        output  : OUT std_logic_vector(15 downto 0)

	);
	
END pid_controller;


ARCHITECTURE arch OF pid_controller IS

	signal integrall : std_logic_vector(15 downto 0);
	
BEGIN

process (clk, init, init_val)
	variable kperror : integer range -2147483647 to 2147483647;
	variable kierror : integer range -2147483647 to 2147483647;
begin
if (init = '1') then
	integrall <= init_val;
	output <= init_val;
else
	if (clk'event and clk = '1') then
		if (en = '1') then
			kperror := conv_integer(kp) * conv_integer(error);
			kierror := conv_integer(ki) * conv_integer(error);
			if (conv_integer(integrall) < 65000) then 	-- 65000
				integrall <= integrall + conv_std_logic_vector(kierror, 32)(31 downto 16);
			end if;
			
			output <= conv_std_logic_vector(kperror, 32)(31 downto 16) + integrall;
		end if;
	end if;
end if;
end process;

end architecture;
