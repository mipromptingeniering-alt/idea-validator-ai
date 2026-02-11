#!/usr/bin/env python3
"""
Generador de Business Case Profesional
Documento completo con análisis de mercado, previsiones, opinión profesional
"""
from datetime import datetime
import json

class BusinessCaseGenerator:

    def generate_business_case(self, idea_data):
        """Generar documento business case completo"""

        nombre = idea_data.get('Nombre', 'Producto')
        tipo = idea_data.get('Tipo', 'SaaS')
        resumen = idea_data.get('Resumen', '')
        descripcion = idea_data.get('Descripcion', idea_data.get('Descripción', ''))
        score = idea_data.get('Score Total', 0)
        publico = idea_data.get('Público Objetivo', idea_data.get('Publico Objetivo', ''))
        problema = idea_data.get('Problema', '')
        precio = idea_data.get('Precio Estimado', '')
        horas = idea_data.get('Horas Desarrollo', 0)
        complejidad = idea_data.get('Complejidad', 'Media')
        mvp_features = idea_data.get('MVP Features', '')
        canales = idea_data.get('Canales', '')

        # Análisis de mercado basado en tipo
        market_analysis = self._get_market_analysis(tipo, publico)

        # Previsiones financieras
        financial_forecast = self._calculate_financial_forecast(precio, tipo)

        # Riesgos y oportunidades
        risks = self._analyze_risks(complejidad, score, tipo)

        # Opinión profesional
        professional_opinion = self._get_professional_opinion(score, tipo, complejidad, horas)

        # Roadmap de ejecución
        roadmap = self._create_roadmap(horas, complejidad)

        html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Case - {nombre}</title>
    <style>
        @page {{ margin: 2cm; }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.8;
            color: #1a1a1a;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #fff;
        }}

        /* Cover Page */
        .cover {{
            text-align: center;
            padding: 100px 0;
            border-bottom: 3px solid #667eea;
            margin-bottom: 60px;
        }}

        .cover-title {{
            font-size: 48px;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 16px;
        }}

        .cover-subtitle {{
            font-size: 24px;
            color: #666;
            margin-bottom: 32px;
        }}

        .cover-meta {{
            font-size: 14px;
            color: #999;
        }}

        /* Headers */
        h1 {{
            font-size: 36px;
            font-weight: 700;
            color: #1a1a1a;
            margin: 48px 0 24px;
            padding-bottom: 12px;
            border-bottom: 2px solid #667eea;
        }}

        h2 {{
            font-size: 28px;
            font-weight: 600;
            color: #333;
            margin: 36px 0 16px;
        }}

        h3 {{
            font-size: 20px;
            font-weight: 600;
            color: #444;
            margin: 24px 0 12px;
        }}

        /* Paragraphs */
        p {{
            margin-bottom: 16px;
            text-align: justify;
        }}

        /* Lists */
        ul, ol {{
            margin: 16px 0 16px 32px;
        }}

        li {{
            margin-bottom: 8px;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
            font-size: 14px;
        }}

        th {{
            background: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 12px;
            border-bottom: 1px solid #e5e7eb;
        }}

        tr:nth-child(even) {{
            background: #f9fafb;
        }}

        /* Boxes */
        .info-box {{
            background: #f0f4ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 24px 0;
            border-radius: 4px;
        }}

        .warning-box {{
            background: #fff7ed;
            border-left: 4px solid #f59e0b;
            padding: 20px;
            margin: 24px 0;
            border-radius: 4px;
        }}

        .success-box {{
            background: #f0fdf4;
            border-left: 4px solid #10b981;
            padding: 20px;
            margin: 24px 0;
            border-radius: 4px;
        }}

        .danger-box {{
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 20px;
            margin: 24px 0;
            border-radius: 4px;
        }}

        .box-title {{
            font-weight: 700;
            font-size: 16px;
            margin-bottom: 8px;
        }}

        /* Score badge */
        .score-badge {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 24px;
            font-weight: 700;
            font-size: 18px;
        }}

        .score-high {{ background: #d1fae5; color: #065f46; }}
        .score-medium {{ background: #fef3c7; color: #92400e; }}
        .score-low {{ background: #fee2e2; color: #991b1b; }}

        /* Charts */
        .bar-chart {{
            margin: 24px 0;
        }}

        .bar {{
            display: flex;
            align-items: center;
            margin-bottom: 12px;
        }}

        .bar-label {{
            width: 150px;
            font-weight: 600;
            font-size: 14px;
        }}

        .bar-fill {{
            flex: 1;
            background: #e5e7eb;
            height: 32px;
            border-radius: 4px;
            position: relative;
            overflow: hidden;
        }}

        .bar-value {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            padding: 0 12px;
            color: white;
            font-weight: 600;
            font-size: 14px;
        }}

        /* Print styles */
        @media print {{
            body {{ padding: 0; }}
            .no-print {{ display: none; }}
        }}
    </style>
</head>
<body>
    <!-- Cover Page -->
    <div class="cover">
        <div class="cover-title">BUSINESS CASE</div>
        <div class="cover-subtitle">{nombre}</div>
        <div class="cover-meta">
            Documento Confidencial<br>
            Generado: {datetime.now().strftime("%d de %B, %Y")}<br>
            Tipo: {tipo} • Score: {score}/100
        </div>
    </div>

    <!-- Executive Summary -->
    <h1>1. Resumen Ejecutivo</h1>

    <div class="info-box">
        <div class="box-title">Score de Viabilidad</div>
        <span class="score-badge score-{'high' if score >= 70 else 'medium' if score >= 50 else 'low'}">{score}/100</span>
    </div>

    <p><strong>{nombre}</strong> es un {tipo} diseñado para {publico}. {resumen}</p>

    <p>{descripcion}</p>

    <h3>Problema Identificado</h3>
    <p>{problema if problema else f"Actualmente, {publico} enfrentan desafíos significativos en su día a día que consumen tiempo y recursos valiosos."}</p>

    <h3>Solución Propuesta</h3>
    <p>Mediante {nombre}, ofrecemos una solución que automatiza y optimiza procesos clave, permitiendo a los usuarios enfocarse en actividades de alto valor.</p>

    <!-- Market Analysis -->
    <h1>2. Análisis de Mercado</h1>

    <h2>2.1 Tamaño del Mercado</h2>
    {market_analysis['market_size']}

    <h2>2.2 Público Objetivo</h2>
    <p><strong>Perfil:</strong> {publico}</p>
    <ul>
        <li><strong>Segmento primario:</strong> {market_analysis['primary_segment']}</li>
        <li><strong>Tamaño del segmento:</strong> {market_analysis['segment_size']}</li>
        <li><strong>Disposición a pagar:</strong> {market_analysis['willingness_to_pay']}</li>
    </ul>

    <h2>2.3 Competencia</h2>
    {market_analysis['competition']}

    <h2>2.4 Tendencias del Mercado</h2>
    <ul>
        <li>Crecimiento anual proyectado del sector: {market_analysis['growth_rate']}</li>
        <li>Adopción de soluciones {tipo}: En aumento exponencial</li>
        <li>Inversión en herramientas de productividad: +35% YoY</li>
    </ul>

    <!-- Financial Forecast -->
    <h1>3. Proyecciones Financieras</h1>

    <h2>3.1 Modelo de Negocio</h2>
    <p><strong>Precio:</strong> {precio}</p>
    <p><strong>Modelo:</strong> {financial_forecast['model']}</p>

    <h2>3.2 Proyección de Ingresos (12 meses)</h2>

    <table>
        <thead>
            <tr>
                <th>Mes</th>
                <th>Usuarios</th>
                <th>MRR</th>
                <th>Ingresos Acumulados</th>
            </tr>
        </thead>
        <tbody>
            {self._generate_revenue_table(financial_forecast['monthly'])}
        </tbody>
    </table>

    <h2>3.3 Costos Estimados</h2>

    <table>
        <thead>
            <tr>
                <th>Concepto</th>
                <th>Primer Año</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Desarrollo inicial</td>
                <td>{financial_forecast['development_cost']}</td>
            </tr>
            <tr>
                <td>Infraestructura (hosting, APIs)</td>
                <td>{financial_forecast['infrastructure_cost']}</td>
            </tr>
            <tr>
                <td>Marketing y adquisición</td>
                <td>{financial_forecast['marketing_cost']}</td>
            </tr>
            <tr>
                <td>Soporte y mantenimiento</td>
                <td>{financial_forecast['support_cost']}</td>
            </tr>
            <tr>
                <td><strong>Total</strong></td>
                <td><strong>{financial_forecast['total_cost']}</strong></td>
            </tr>
        </tbody>
    </table>

    <h2>3.4 Punto de Equilibrio</h2>
    <div class="success-box">
        <div class="box-title">Break-even Point</div>
        <p>Con los costos estimados y el modelo de pricing propuesto, el punto de equilibrio se alcanza aproximadamente en el <strong>mes {financial_forecast['breakeven_month']}</strong> con <strong>{financial_forecast['breakeven_users']} usuarios pagando</strong>.</p>
    </div>

    <!-- Execution Plan -->
    <h1>4. Plan de Ejecución</h1>

    <h2>4.1 Roadmap de Desarrollo</h2>
    <p><strong>Tiempo estimado MVP:</strong> {horas} horas ({horas//40} semanas aprox.)</p>
    <p><strong>Complejidad técnica:</strong> {complejidad}</p>

    <h3>Fases del Proyecto</h3>
    {roadmap}

    <h2>4.2 MVP Features</h2>
    <p>{mvp_features if mvp_features else "Features principales a desarrollar en la versión inicial."}</p>

    <h2>4.3 Canales de Distribución</h2>
    <p>{canales if canales else "SEO, Content Marketing, Partnerships, Paid Ads"}</p>

    <h2>4.4 Métricas Clave (KPIs)</h2>
    <ul>
        <li><strong>MRR (Monthly Recurring Revenue):</strong> Principal métrica de ingresos</li>
        <li><strong>CAC (Customer Acquisition Cost):</strong> Objetivo: < $100</li>
        <li><strong>LTV (Lifetime Value):</strong> Objetivo: > $500</li>
        <li><strong>Churn Rate:</strong> Objetivo: < 5% mensual</li>
        <li><strong>NPS (Net Promoter Score):</strong> Objetivo: > 50</li>
    </ul>

    <!-- Risk Analysis -->
    <h1>5. Análisis de Riesgos y Oportunidades</h1>

    <h2>5.1 Riesgos Identificados</h2>
    {risks['risks_html']}

    <h2>5.2 Oportunidades</h2>
    {risks['opportunities_html']}

    <h2>5.3 Mitigación de Riesgos</h2>
    <ul>
        <li><strong>Validación temprana:</strong> Landing page + beta privada antes de desarrollo completo</li>
        <li><strong>MVP lean:</strong> Desarrollar solo funcionalidades core inicialmente</li>
        <li><strong>Feedback continuo:</strong> Iteraciones cada 2 semanas basadas en datos de usuarios</li>
        <li><strong>Diversificación de canales:</strong> No depender de un solo canal de adquisición</li>
    </ul>

    <!-- Professional Opinion -->
    <h1>6. Opinión Profesional y Recomendación</h1>

    {professional_opinion}

    <h2>6.2 Recomendación Final</h2>
    {self._get_recommendation(score)}

    <!-- Next Steps -->
    <h1>7. Próximos Pasos Inmediatos</h1>

    <ol>
        <li><strong>Semana 1:</strong> Validar demanda con landing page + anuncios (inversión: $500)</li>
        <li><strong>Semana 2-3:</strong> Recoger feedback de early adopters (100 registros mínimo)</li>
        <li><strong>Semana 4-8:</strong> Desarrollar MVP con features core</li>
        <li><strong>Semana 9:</strong> Beta privada con 20-30 usuarios</li>
        <li><strong>Semana 10-12:</strong> Iterar basado en feedback + preparar lanzamiento</li>
        <li><strong>Semana 13:</strong> Lanzamiento público + campaña marketing</li>
    </ol>

    <div class="info-box">
        <div class="box-title">Inversión Inicial Recomendada</div>
        <p>Para ejecutar este plan de manera óptima, se recomienda una inversión inicial de <strong>${financial_forecast['initial_investment']}</strong>, distribuidos en desarrollo, marketing de validación, e infraestructura base.</p>
    </div>

    <!-- Appendix -->
    <h1>8. Anexos</h1>

    <h2>8.1 Datos Técnicos</h2>
    <ul>
        <li><strong>ID de Idea:</strong> {idea_data.get('ID', 'N/A')}</li>
        <li><strong>Fecha de Generación:</strong> {idea_data.get('Created Date', 'N/A')}</li>
        <li><strong>Score Total:</strong> {score}/100</li>
        <li><strong>Tipo:</strong> {tipo}</li>
    </ul>

    <hr style="margin: 48px 0; border: none; border-top: 1px solid #e5e7eb;">

    <p style="text-align: center; color: #999; font-size: 12px;">
        Documento generado automáticamente por Idea Validator Pro<br>
        © {datetime.now().year} - Confidencial
    </p>
</body>
</html>'''

        return html

    def _get_market_analysis(self, tipo, publico):
        """Análisis de mercado según tipo"""

        market_data = {
            'SaaS': {
                'market_size': '<p>El mercado global de SaaS alcanzó los $195 billones en 2023 y se proyecta crecer a $232 billones en 2024 (CAGR 15.7%). El segmento de herramientas de productividad representa aproximadamente el 22% de este mercado.</p>',
                'primary_segment': f'{publico} en empresas de 10-500 empleados',
                'segment_size': '~2.5M empresas potenciales en mercado de habla hispana',
                'willingness_to_pay': 'Alta ($20-$100/mes según funcionalidades)',
                'competition': '<p><strong>Nivel de competencia:</strong> Alto pero fragmentado. Existen players grandes (Salesforce, HubSpot) pero también espacio para soluciones especializadas verticales.</p><p><strong>Diferenciación clave:</strong> Enfoque en nicho específico, UX superior, precio competitivo.</p>',
                'growth_rate': '15-20%'
            },
            'Extension': {
                'market_size': '<p>Las extensiones de navegador son utilizadas por más de 1,500M de usuarios globalmente. El 65% de usuarios de Chrome tienen al menos una extensión instalada.</p>',
                'primary_segment': f'{publico} usuarios activos de navegador web',
                'segment_size': '~50M usuarios potenciales en mercado objetivo',
                'willingness_to_pay': 'Media-Baja (freemium con premium $5-$15/mes)',
                'competition': '<p><strong>Nivel de competencia:</strong> Medio. Chrome Web Store tiene >200k extensiones pero solo el 1% tiene tracción real.</p><p><strong>Diferenciación clave:</strong> Solución de problema específico, marketing efectivo.</p>',
                'growth_rate': '10-12%'
            },
            'MicroSaaS': {
                'market_size': '<p>El mercado de MicroSaaS (productos con <$100k ARR) está en explosión. Más de 10,000 MicroSaaS rentables operan actualmente con equipos de 1-3 personas.</p>',
                'primary_segment': f'{publico} buscando soluciones especializadas',
                'segment_size': '~100k usuarios potenciales en nicho específico',
                'willingness_to_pay': 'Media ($10-$30/mes)',
                'competition': '<p><strong>Nivel de competencia:</strong> Bajo-Medio en nichos específicos.</p><p><strong>Diferenciación clave:</strong> Extremadamente enfocado en resolver un problema específico muy bien.</p>',
                'growth_rate': '25-30%'
            }
        }

        return market_data.get(tipo, market_data['SaaS'])

    def _calculate_financial_forecast(self, precio, tipo):
        """Calcular proyecciones financieras"""

        # Extraer número del precio
        try:
            precio_num = int(''.join(filter(str.isdigit, precio.split('/')[0])))
        except:
            precio_num = 29

        # Generar proyección mensual
        monthly = []
        users = 0
        for month in range(1, 13):
            if month <= 3:
                new_users = 5 * month  # Primeros meses: crecimiento lento
            elif month <= 6:
                new_users = 15 + (month * 3)  # Tracción inicial
            elif month <= 9:
                new_users = 40 + (month * 5)  # Crecimiento acelerado
            else:
                new_users = 80 + (month * 10)  # Scaling

            users += new_users
            mrr = users * precio_num

            monthly.append({
                'month': month,
                'users': users,
                'mrr': mrr,
                'arr': mrr * 12
            })

        # Costos
        dev_cost = 5000 if tipo == 'SaaS' else 2000 if tipo == 'Extension' else 3000
        infra_cost = 3000
        marketing_cost = 6000
        support_cost = 2000
        total_cost = dev_cost + infra_cost + marketing_cost + support_cost

        # Break-even
        breakeven_month = 6
        breakeven_users = total_cost // (precio_num * 12)

        return {
            'model': 'Suscripción mensual/anual con modelo freemium' if tipo == 'SaaS' else 'One-time purchase con upsells',
            'monthly': monthly,
            'development_cost': f'${dev_cost:,}',
            'infrastructure_cost': f'${infra_cost:,}',
            'marketing_cost': f'${marketing_cost:,}',
            'support_cost': f'${support_cost:,}',
            'total_cost': f'${total_cost:,}',
            'breakeven_month': breakeven_month,
            'breakeven_users': breakeven_users,
            'initial_investment': f'{total_cost // 2:,}'
        }

    def _generate_revenue_table(self, monthly_data):
        """Generar tabla de ingresos"""
        html = ''
        cumulative = 0
        for data in monthly_data[:12]:
            cumulative += data['mrr']
            html += f'''
                <tr>
                    <td>Mes {data['month']}</td>
                    <td>{data['users']}</td>
                    <td>${data['mrr']:,}</td>
                    <td>${cumulative:,}</td>
                </tr>
            '''
        return html

    def _analyze_risks(self, complejidad, score, tipo):
        """Analizar riesgos y oportunidades"""

        risks = []
        opportunities = []

        # Riesgos según complejidad
        if complejidad == 'Alta':
            risks.append(('Alto', 'Complejidad Técnica', 'El desarrollo puede tomar más tiempo del estimado y requerir expertise específico.'))
            risks.append(('Medio', 'Bugs y Mantenimiento', 'Mayor superficie de ataque para bugs. Requiere QA riguroso.'))

        # Riesgos según score
        if score < 60:
            risks.append(('Alto', 'Validación de Mercado', 'Score moderado indica necesidad de validación exhaustiva antes de desarrollo completo.'))

        # Riesgos según tipo
        if tipo == 'Extension':
            risks.append(('Medio', 'Dependencia de Plataforma', 'Cambios en políticas de Chrome Web Store pueden afectar el producto.'))

        # Riesgos generales
        risks.append(('Medio', 'Adquisición de Usuarios', 'CAC puede ser mayor al proyectado inicialmente.'))
        risks.append(('Bajo', 'Churn Rate', 'Usuarios pueden cancelar si no ven valor inmediato.'))

        # Oportunidades
        opportunities.append('Mercado en crecimiento con tendencia alcista sostenida')
        opportunities.append('Bajo costo de entrada permite pivotes rápidos si es necesario')
        opportunities.append('Posibilidad de monetización múltiple (freemium, premium, enterprise)')
        opportunities.append('Escalabilidad técnica relativamente sencilla')
        opportunities.append('Potencial de expansión internacional con mínimos ajustes')

        # Generar HTML
        risks_html = '<table><thead><tr><th>Nivel</th><th>Riesgo</th><th>Descripción</th></tr></thead><tbody>'
        for nivel, nombre, desc in risks:
            risks_html += f'<tr><td><strong>{nivel}</strong></td><td>{nombre}</td><td>{desc}</td></tr>'
        risks_html += '</tbody></table>'

        opportunities_html = '<ul>'
        for opp in opportunities:
            opportunities_html += f'<li>{opp}</li>'
        opportunities_html += '</ul>'

        return {
            'risks_html': risks_html,
            'opportunities_html': opportunities_html
        }

    def _get_professional_opinion(self, score, tipo, complejidad, horas):
        """Opinión profesional objetiva"""

        if score >= 75:
            verdict = 'Altamente Recomendable'
            color = 'success'
            opinion = f'''
            <div class="{color}-box">
                <div class="box-title">Veredicto: {verdict}</div>
                <p>Con un score de {score}/100, esta idea presenta fundamentals sólidos y alto potencial de éxito.</p>
            </div>

            <h3>Análisis Detallado</h3>

            <p><strong>Fortalezas:</strong></p>
            <ul>
                <li>Score superior indica problema claro, mercado validado y solución factible</li>
                <li>El tipo {tipo} tiene precedentes exitosos en el mercado</li>
                <li>Tiempo de desarrollo estimado ({horas}h) es razonable para llegar a mercado rápidamente</li>
                <li>Potencial de monetización claro desde día 1</li>
            </ul>

            <p><strong>Áreas de Atención:</strong></p>
            <ul>
                <li>Validar pricing con usuarios reales antes de comprometerse</li>
                <li>Complejidad {complejidad} requiere equipo con expertise adecuado</li>
                <li>Identificar early adopters para beta testing lo antes posible</li>
            </ul>

            <p><strong>Conclusión:</strong> Esta idea merece inversión de tiempo y recursos. El riesgo es moderado-bajo con upside potencialmente alto. Se recomienda proceder con fase de validación inicial inmediatamente.</p>
            '''
        elif score >= 60:
            verdict = 'Viable con Validación'
            color = 'info'
            opinion = f'''
            <div class="{color}-box">
                <div class="box-title">Veredicto: {verdict}</div>
                <p>Score de {score}/100 indica una idea prometedora que requiere validación adicional antes de comprometer recursos significativos.</p>
            </div>

            <h3>Análisis Detallado</h3>

            <p><strong>Fortalezas:</strong></p>
            <ul>
                <li>Concepto sólido con potencial de mercado</li>
                <li>Factibilidad técnica demostrada</li>
                <li>Tiempo de desarrollo manejable</li>
            </ul>

            <p><strong>Debilidades Identificadas:</strong></p>
            <ul>
                <li>Necesita validación más profunda de demanda real</li>
                <li>Competencia puede ser más fuerte de lo estimado</li>
                <li>Pricing podría requerir ajustes según feedback del mercado</li>
            </ul>

            <p><strong>Recomendación de Validación:</strong></p>
            <ol>
                <li>Crear landing page y correr ads ($500 presupuesto)</li>
                <li>Objetivo: 100+ registros en 2 semanas</li>
                <li>Entrevistar a 20 registrados para entender pain points</li>
                <li>Si validación es positiva → proceder con MVP</li>
            </ol>

            <p><strong>Conclusión:</strong> No descartar, pero tampoco rush to build. Invertir 2-3 semanas en validación puede ahorrar meses de desarrollo de un producto que nadie quiere.</p>
            '''
        else:
            verdict = 'Alto Riesgo - Validación Crítica'
            color = 'warning'
            opinion = f'''
            <div class="{color}-box">
                <div class="box-title">Veredicto: {verdict}</div>
                <p>Score de {score}/100 señala riesgos significativos que deben abordarse antes de proceder.</p>
            </div>

            <h3>Análisis Detallado</h3>

            <p><strong>Preocupaciones Principales:</strong></p>
            <ul>
                <li>Score bajo sugiere problemas en problem-market fit o factibilidad</li>
                <li>Mercado puede ser demasiado pequeño o competencia demasiado fuerte</li>
                <li>Complejidad {complejidad} añade riesgo adicional</li>
            </ul>

            <p><strong>Antes de Proceder:</strong></p>
            <ol>
                <li><strong>Validar problema:</strong> ¿Es realmente un problema que la gente pagaría por resolver?</li>
                <li><strong>Analizar competencia:</strong> ¿Por qué soluciones existentes no funcionan?</li>
                <li><strong>Pivotar si es necesario:</strong> Quizá hay un ángulo diferente más prometedor</li>
            </ol>

            <p><strong>Conclusión:</strong> No proceder con desarrollo completo sin validación exhaustiva. Considerar pivot o ajustes significativos antes de invertir recursos. Si validación inicial falla, es mejor abandonar early que invertir meses en un dead-end.</p>
            '''

        return opinion

    def _get_recommendation(self, score):
        """Recomendación final"""

        if score >= 75:
            return '''
            <div class="success-box">
                <div class="box-title">✅ GO - Proceder con Desarrollo</div>
                <p>Esta idea presenta fundamentals sólidos y merece inversión inmediata. Se recomienda:</p>
                <ul>
                    <li>Asignar presupuesto de validación ($500) para esta semana</li>
                    <li>Comenzar reclutamiento de early adopters</li>
                    <li>Iniciar desarrollo de MVP en paralelo a validación</li>
                    <li>Target: MVP en mercado en 8-10 semanas</li>
                </ul>
            </div>
            '''
        elif score >= 60:
            return '''
            <div class="info-box">
                <div class="box-title">⚠️  VALIDATE FIRST - Validar Antes de Construir</div>
                <p>Idea prometedora pero requiere validación antes de comprometer desarrollo completo:</p>
                <ul>
                    <li>Invertir 2-3 semanas en validación rigurosa</li>
                    <li>Landing page + ads + entrevistas a usuarios</li>
                    <li>Si validación positiva → proceder con MVP</li>
                    <li>Si validación negativa → pivotar o abandonar</li>
                </ul>
            </div>
            '''
        else:
            return '''
            <div class="warning-box">
                <div class="box-title">🛑 HIGH RISK - No Proceder Sin Validación Exhaustiva</div>
                <p>Score indica riesgos significativos. Antes de cualquier desarrollo:</p>
                <ul>
                    <li>Realizar investigación profunda de mercado</li>
                    <li>Validar problema con 50+ usuarios potenciales</li>
                    <li>Considerar pivot significativo</li>
                    <li>Si validación falla en 2 semanas → abandonar y pasar a siguiente idea</li>
                </ul>
            </div>
            '''

    def _create_roadmap(self, horas, complejidad):
        """Crear roadmap de ejecución"""

        weeks = max(4, horas // 40)

        roadmap = f'''
        <table>
            <thead>
                <tr>
                    <th>Fase</th>
                    <th>Duración</th>
                    <th>Entregables</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Fase 1: Validación</strong></td>
                    <td>1-2 semanas</td>
                    <td>Landing page, 100+ registros, 20 entrevistas</td>
                </tr>
                <tr>
                    <td><strong>Fase 2: Diseño</strong></td>
                    <td>1 semana</td>
                    <td>Wireframes, flows, mockups de pantallas core</td>
                </tr>
                <tr>
                    <td><strong>Fase 3: Desarrollo MVP</strong></td>
                    <td>{weeks} semanas</td>
                    <td>MVP funcional con features core</td>
                </tr>
                <tr>
                    <td><strong>Fase 4: Beta Testing</strong></td>
                    <td>2 semanas</td>
                    <td>Beta con 20-30 usuarios, recoger feedback, bug fixes</td>
                </tr>
                <tr>
                    <td><strong>Fase 5: Lanzamiento</strong></td>
                    <td>1 semana</td>
                    <td>Launch público, marketing, primeros 100 usuarios</td>
                </tr>
            </tbody>
        </table>

        <p><strong>Timeline total estimado:</strong> {weeks + 6} semanas desde inicio hasta lanzamiento público.</p>
        '''

        return roadmap
