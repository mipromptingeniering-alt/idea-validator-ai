#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Pages Deployer - Reemplaza a Vercel
Crea landing pages HTML directamente sin encoding corrupto
"""

import os
import json
from datetime import datetime

def deploy_to_github_pages(idea_data):
    """
    Crea landing page HTML y la guarda en carpeta landing-pages/
    """
    try:
        # Crear carpeta si no existe
        os.makedirs('landing-pages', exist_ok=True)
        
        # Crear nombre de archivo único
        idea_id = idea_data.get('ID', 'unknown')
        filename = f"landing-pages/idea-{idea_id}.html"
        
        # Sanitizar texto para HTML
        def sanitize(text):
            if not text:
                return ""
            return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        
              # Guardar archivo HTML
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{sanitize(idea_data.get('Resumen', '')[:150])}">
    <title>{sanitize(idea_data.get('Nombre', 'Idea'))} - Idea Validator AI</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6; 
            color: #1f2937; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; 
            padding: 20px;
        }}
        .container {{ 
            max-width: 900px; 
            margin: 0 auto; 
            background: white; 
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        h1 {{ 
            color: #667eea; 
            font-size: 2.5em; 
            margin-bottom: 20px;
            line-height: 1.2;
        }}
        .score {{ 
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 12px 25px;
            border-radius: 50px;
            display: inline-block;
            font-size: 1.3em;
            font-weight: bold;
            margin: 15px 0;
        }}
        .tag {{ 
            background: #667eea;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            display: inline-block;
            margin: 5px 5px 5px 0;
            font-size: 0.9em;
            font-weight: 500;
        }}
        .section {{ 
            margin: 30px 0;
            padding: 25px;
            background: #f9fafb;
            border-radius: 12px;
            border-left: 4px solid #667eea;
        }}
        .section h2 {{ 
            color: #374151;
            margin-bottom: 15px;
            font-size: 1.4em;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .section p {{ 
            color: #4b5563;
            line-height: 1.8;
            font-size: 1.05em;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        .info-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
        }}
        .info-card strong {{
            color: #667eea;
            display: block;
            margin-bottom: 5px;
        }}
        ul {{ 
            margin-left: 20px;
            margin-top: 10px;
        }}
        li {{ 
            margin: 8px 0;
            color: #4b5563;
            line-height: 1.6;
        }}
        .footer {{ 
            text-align: center;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 2px solid #e5e7eb;
            color: #6b7280;
        }}
        .footer a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 20px; }}
            h1 {{ font-size: 2em; }}
            .info-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 {sanitize(idea_data.get('Nombre', 'Idea de Negocio'))}</h1>
        
        <div>
            <span class="score">📊 Score: {idea_data.get('Score Total', 0)}/100</span>
            <span class="tag">{sanitize(idea_data.get('Tipo', 'Digital'))}</span>
        </div>
        
        <div class="section">
            <h2>📋 Resumen Ejecutivo</h2>
            <p>{sanitize(idea_data.get('Resumen', 'No disponible'))}</p>
        </div>
        
        <div class="section">
            <h2>📖 Descripción Detallada</h2>
            <p>{sanitize(idea_data.get('Descripción', 'No disponible'))}</p>
        </div>
        
        <div class="section">
            <h2>🎯 Público Objetivo</h2>
            <p>{sanitize(idea_data.get('Público Objetivo', 'No especificado'))}</p>
        </div>
        
        <div class="section">
            <h2>❌ Problema que Resuelve</h2>
            <p>{sanitize(idea_data.get('Problema', 'No especificado'))}</p>
        </div>
        
        <div class="section">
            <h2>✅ Solución Propuesta</h2>
            <p>{sanitize(idea_data.get('Solución', 'No especificada'))}</p>
        </div>
        
        <div class="section">
            <h2>⚙️ Características MVP</h2>
            <ul>
                {''.join([f'<li>{sanitize(feature.strip())}</li>' for feature in str(idea_data.get('MVP Features', '')).split(',') if feature.strip()])}
            </ul>
        </div>
        
        <div class="section">
            <h2>📊 Información Técnica y Financiera</h2>
            <div class="info-grid">
                <div class="info-card">
                    <strong>Complejidad</strong>
                    {sanitize(idea_data.get('Complejidad', 'N/A'))}
                </div>
                <div class="info-card">
                    <strong>Horas de Desarrollo</strong>
                    {sanitize(idea_data.get('Horas Desarrollo', 'N/A'))}
                </div>
                <div class="info-card">
                    <strong>Precio Estimado</strong>
                    {sanitize(idea_data.get('Precio Estimado', 'N/A'))}
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>🎯 Canales de Distribución</h2>
            <p>{sanitize(idea_data.get('Canales', 'No especificados'))}</p>
        </div>
        
        <div class="section">
            <h2>🏆 Análisis Competitivo</h2>
            <p><strong>Competencia:</strong> {sanitize(idea_data.get('Competencia', 'No analizada'))}</p>
            <p style="margin-top: 15px;"><strong>Diferenciación:</strong> {sanitize(idea_data.get('Diferenciación', 'No especificada'))}</p>
        </div>
        
        <div class="footer">
            <p>✨ Idea generada automáticamente por <strong>Idea Validator AI</strong></p>
            <p>🤖 Powered by OpenAI GPT-4o-mini</p>
            <p>📅 Creada el {sanitize(idea_data.get('Created Date', datetime.now().strftime('%Y-%m-%d %H:%M')))}</p>
            <p style="margin-top: 15px;"><a href="index.html">← Volver al listado de ideas</a></p>
        </div>
    </div>
</body>
</html>"""
        
        # Guardar archivo HTML
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # URL relativa para GitHub Pages
        landing_url = f"idea-{idea_id}.html"
        
        print(f"✅ Landing page creada: {filename}")
        return landing_url, True
        
    except Exception as e:
        print(f"❌ Error creando landing page: {str(e)}")
        import traceback
        traceback.print_exc()
        return "", False

def update_ideas_list():
    """
    Actualiza el archivo JSON con listado de todas las ideas para el índice
    """
    try:
        import pandas as pd
        
        csv_path = 'data/ideas-validadas.csv'
        if not os.path.exists(csv_path):
            print("⚠️ CSV no encontrado")
            return
        
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        
        if df.empty:
            print("⚠️ CSV vacío")
            return
        
        ideas_list = []
        for _, row in df.iterrows():
            ideas_list.append({
                'nombre': str(row.get('Nombre', 'Sin nombre')),
                'tipo': str(row.get('Tipo', 'Digital')),
                'resumen': str(row.get('Resumen', ''))[:150] + ('...' if len(str(row.get('Resumen', ''))) > 150 else ''),
                'score': int(row.get('Score Total', 0)),
                'landing_url': str(row.get('Landing URL', ''))
            })
        
        # Ordenar por score descendente
        ideas_list.sort(key=lambda x: x['score'], reverse=True)
        
        # Guardar JSON
        os.makedirs('landing-pages', exist_ok=True)
        with open('landing-pages/ideas-list.json', 'w', encoding='utf-8') as f:
            json.dump(ideas_list, f, ensure_ascii=False, indent=2)
            
        print(f"✅ Lista de ideas actualizada: {len(ideas_list)} ideas")
        
    except Exception as e:
        print(f"❌ Error actualizando lista: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🧪 Test del deployer...")
    # Test básico
    test_idea = {
        'ID': 'test-001',
        'Nombre': 'Test Idea',
        'Tipo': 'SaaS',
        'Resumen': 'Una idea de prueba',
        'Descripción': 'Descripción de prueba',
        'Score Total': 75
    }
    url, success = deploy_to_github_pages(test_idea)
    print(f"Resultado: {'✅ Éxito' if success else '❌ Error'}")
    print(f"URL: {url}")
