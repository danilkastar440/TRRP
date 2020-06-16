<h1><b>Нормализация бд</b></h1><br>
Использованные СУБД: sqlite3 & MySQL <br>
Язык программирования: Python3 <br>
Как использовать: <br>
1. Для считывания и нормализации данных из sqlite3 в MySQL: <b>python3 normalize.py --filename baza.db</b> <br>  
2. Для экспорта из MySQL в xlsx: <b>python3 normalize.py --export</b> <br><br>
  

  
Выполненные требования задания:
  1. Выбрана предметная область(машины) и спроектированы базы данных: <br>
    - Нормализованная в 5 таблицах 
      <table>
      <h2><b> Cars </b><h2>
      <tr>
        <th>model</th>
        <th>brand</th>
        <th>engine</th>
        <th>transmissins</th>
        <th>price</th>
        <th>wheel</th>
      </tr>
      <tr><td>2114</td><td>LADA</td><td>V123</td><td>M123</td><td>100000</td><td>Best kolesa</td></tr>
      <tr><td>2115</td><td>LADA</td><td>V124</td><td>M124</td><td>150000</td><td>Not best kolesa</td></tr>
      <tr><td>Rio</td><td>Kia</td><td>V14234</td><td>A1234</td><td>400000</td><td>Best kolesa</td></tr>
      <tr><td>Sportage</td><td>Kia</td><td>V12332</td><td>A123</td><td>500000</td><td>THE best kolesa</td></tr>
      <tr><td>911</td><td>Porsche</td><td>E2312</td><td>R123</td><td>3000000</td><td>THE Bbst kolesa</td></tr>
      </table>
        <br><br>
      <table>
      <h2><b> Brands </b><h2>
      <tr>
        <th>brand_name</th>
        <th>brand_creator_country</th>
      </tr>
      <tr><td>Kia</td><td>Korea</td>
      <tr><td>LADA</td><td>Russia</td>
      <tr><td>Porsche</td><td>Germany</td>
      </table>
       <br><br>
      <table>
      <h2><b> Engines </b><h2>
      <tr>
        <th>engine_model</th>
        <th>engine_power</th>
        <th>engine_volume</th>
        <th>engine_type</th>
      </tr>
      <tr><td>E2312</td><td>300</td><td>50</td><td>V12</td>
      <tr><td>V123</td><td>80</td><td>16</td><td>L4</td>
      <tr><td>V12332</td><td>100</td><td>90</td><td>V4</td>
      <tr><td>V124</td><td>100</td><td>18</td><td>L4</td>
      <tr><td>V14234</td><td>100</td><td>90</td><td>V4</td>
      </table>
       <br><br>
      <table>
      <h2><b> Transmissions </b><h2>
      <tr>
        <th>transmission_model</th>
        <th>transmission_type</th>
        <th>transmission_gears_number</th>
      </tr>
      <tr><td>A123</td><td>A</td><td>5</td>
      <tr><td>A1234</td><td>A</td><td>4</td>
      <tr><td>M123</td><td>M</td><td>5</td>
      <tr><td>R123</td><td>A</td><td>8</td>
      </table>
       <br><br>
      <table>
      <h2><b> Wheels </b><h2>
      <tr>
        <th>wheel_model</th>
        <th>wheel_radius</th>
        <th>wheel_color</th>
      </tr>
      <tr><td>Best kolesa</td><td>13</td><td>White</td>
      <tr><td>Not best kolesa</td><td>13</td><td>Black</td>
      <tr><td>THE best kolesa</td><td>15</td><td>Yellow</td>
      </table>
      <br><br>
- Ненормализованная в 1 таблице:
<table class="table table-bordered table-hover table-condensed">
  <h2><b> Cars </b><h2>
<table class="table table-bordered table-hover table-condensed">
<thead><tr><th title="Field #1">Model</th>
<th title="Field #2">BrandName</th>
<th title="Field #3">BrandCreatorCountry</th>
<th title="Field #4">EngineModel</th>
<th title="Field #5">EnginePower</th>
<th title="Field #6">EngineVolume</th>
<th title="Field #7">EngineType</th>
<th title="Field #8">TransmissionModel</th>
<th title="Field #9">TransmissionType</th>
<th title="Field #10">TransmissionGearsNumber</th>
<th title="Field #11">WheelModel</th>
<th title="Field #12">WheelRadius</th>
<th title="Field #13">WheelColor</th>
<th title="Field #14">Price</th>
</tr></thead>
<tbody><tr>
<td>2114</td>
<td>LADA</td>
<td>Russia</td>
<td>V123</td>
<td align="right">80</td>
<td align="right">16</td>
<td>L4</td>
<td>M123</td>
<td>M</td>
<td align="right">5</td>
<td>Best kolesa</td>
<td align="right">13</td>
<td>White</td>
<td align="right">100000</td>
</tr>
<tr>
<td>2115</td>
<td>LADA</td>
<td>Russia</td>
<td>V124</td>
<td align="right">100</td>
<td align="right">18</td>
<td>L4</td>
<td>M123</td>
<td>M</td>
<td align="right">5</td>
<td>Not best kolesa</td>
<td align="right">13</td>
<td>Black</td>
<td align="right">150000</td>
</tr>
<tr>
<td>Rio</td>
<td>Kia</td>
<td>Korea</td>
<td>V14234</td>
<td align="right">100</td>
<td align="right">90</td>
<td>V4</td>
<td>A1234</td>
<td>A</td>
<td align="right">4</td>
<td>Best kolesa</td>
<td align="right">15</td>
<td>Red</td>
<td align="right">400000</td>
</tr>
<tr>
<td>Sportage</td>
<td>Kia</td>
<td>Korea</td>
<td>V12323</td>
<td align="right">100</td>
<td align="right">90</td>
<td>V4</td>
<td>A123</td>
<td>A</td>
<td align="right">5</td>
<td>THE best kolesa</td>
<td align="right">15</td>
<td>Yellow</td>
<td align="right">500000</td>
</tr>
<tr>
<td>911</td>
<td>Porsche</td>
<td>Germany</td>
<td>E2312</td>
<td align="right">300</td>
<td align="right">50</td>
<td>V12</td>
<td>R123</td>
<td>A</td>
<td align="right">8</td>
<td>THE best kolesa</td>
<td align="right">20</td>
<td>Blue</td>
<td align="right">3000000</td>
</tr>
</tbody></table>
    
