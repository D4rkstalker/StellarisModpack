Includes = {
	"terra_incognita.fxh"
}

PixelShader =
{
	Samplers =
	{
		NebulaTexture =
		{
			Index = 0;
			MagFilter = "Linear";
			MinFilter = "Linear";
			AddressU = "Wrap";
			AddressV = "Wrap";
		}

		ColorTexture =
		{
			Index = 1;
			MagFilter = "Linear";
			MinFilter = "Linear";
			AddressU = "Wrap";
			AddressV = "Wrap";
		}

		TerraIncognitaTexture =
		{
			Index = 2;
			MagFilter = "Linear";
			MinFilter = "Linear";
			AddressU = "Clamp"
			AddressV = "Clamp"
		}

		Border = {
			Index = 3;
			MagFilter = "Linear";
			MinFilter = "Linear";
			MipFilter = "none";
			AddressU = "Wrap";
			AddressV = "Wrap";
		}
	}
}

VertexStruct VS_INPUT
{
    float2 vPosition  		: POSITION;
	float2 vUV				: TEXCOORD0;
	float3 vPos				: TEXCOORD1;
	float2 vSize_vRot		: TEXCOORD2;
};

VertexStruct VS_OUTPUT
{
    float4 vPosition 	: PDX_POSITION;
	float2 vUV			: TEXCOORD0;
	float2 vPos			: TEXCOORD1;
	float4 vScreenCoord : TEXCOORD2;
};

ConstantBuffer( Common, 0, 0 )
{
	float4x4 	ViewProjectionMatrix;
	float4		TimeRot;
};

VertexShader =
{
	MainCode VertexShader
		ConstantBuffers = { Common }
	[[
		VS_OUTPUT main(const VS_INPUT v )
		{
			VS_OUTPUT Out;
			float4 vPos = float4( v.vPosition.x, -9.0f, v.vPosition.y, 1.0f );
			vPos.xz *= v.vSize_vRot.x;
			float vTimeRot = TimeRot.x * ( -saturate( -v.vSize_vRot.y * 1000.0f ) + saturate( v.vSize_vRot.y * 1000.0f ) );
			float randSin = sin( v.vSize_vRot.y + vTimeRot );
			float randCos = cos( v.vSize_vRot.y + vTimeRot );

			vPos.xz = float2(
				vPos.x * randCos - vPos.z * randSin,
				vPos.x * randSin + vPos.z * randCos );

			vPos.xyz += v.vPos;
			vPos.y += ( v.vPosition.x + v.vPosition.y ) * 0.5f * 10.f;

			Out.vPosition  	= mul( ViewProjectionMatrix, vPos );
			Out.vUV			= v.vUV;
			Out.vPos		= vPos.xz;

			Out.vScreenCoord.x = ( Out.vPosition.x * 0.5 + Out.vPosition.w * 0.5 );
			Out.vScreenCoord.y = ( Out.vPosition.w * 0.5 - Out.vPosition.y * 0.5 ); //MOD
		#ifdef PDX_OPENGL
			Out.vScreenCoord.y = -Out.vScreenCoord.y;
		#endif
			Out.vScreenCoord.z = Out.vPosition.w;
			Out.vScreenCoord.w = Out.vPosition.w;

			return Out;
		}

	]]
}

PixelShader =
{
	MainCode PixelShader
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float4 vDiffuse = tex2D( NebulaTexture, v.vUV );
			vDiffuse.a = saturate( vDiffuse.a * 6.0f );
			float4 vColor = tex2D( ColorTexture, v.vUV  );

			float vTI = CalcTerraIncognitaValue( v.vPos.xy, TerraIncognitaTexture );

			float4 vBorderColor = tex2Dproj( Border, v.vScreenCoord );

			vBorderColor.a = saturate( vBorderColor.a * 0.1f ); // 0.5
			vColor.rgb = lerp( vColor.rgb, vBorderColor.rgb * 0.1f,  vBorderColor.a ); // was 2.0 - doesn't make borders brighter above nebulas

			float4 vTIColor = ApplyTerraIncognitaValue( vColor, TI_GRAY_BRIGHTNESS, vTI );

			float vBorderTI = 0.8f; // Saturate border under TI
			vTI = saturate( vTI + ( vBorderColor.a * vBorderTI ) * saturate( ( 1.0f - vTI ) * 1000 ) );

			vColor = vDiffuse * lerp( vColor, vTIColor + vBorderColor.a * 0.1f, 1.0f - vTI );

			return vColor;
		}

	]]
}

DepthStencilState DepthStencilState
{
	DepthEnable = no
}

BlendState BlendState
{
	BlendEnable = yes
	AlphaTest = no
	SourceBlend = "SRC_ALPHA"
	DestBlend = "INV_SRC_ALPHA"
}

RasterizerState RasterizerState
{
	FillMode = "FILL_SOLID"
	CullMode = "CULL_NONE"
	FrontCCW = no
}


Effect GalaxyNebula
{
	VertexShader = "VertexShader";
	PixelShader = "PixelShader";
}
