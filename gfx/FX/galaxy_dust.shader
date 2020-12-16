Includes = {
	"terra_incognita.fxh"
}

PixelShader =
{
	Samplers =
	{
		DustTexture =
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
			AddressU = "Clamp";
			AddressV = "Clamp";
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
	float2 vUVColor		: TEXCOORD1;
	float4 vPos			: TEXCOORD2;
	float4 vScreenCoord : TEXCOORD3;
};

ConstantBuffer( Common, 0, 0 )
{
	float4x4 	ViewProjectionMatrix;
	float4		DustCloudUV;
	float2		vResolution;
	float		TimeRot;
};

VertexShader =
{
	MainCode VertexShader
		ConstantBuffers = { Common }
	[[
		VS_OUTPUT main(const VS_INPUT v )
		{
			VS_OUTPUT Out;
			float4 vPos = float4( v.vPosition.x, 0.f, v.vPosition.y, 1.0f );
			vPos.xz *= v.vSize_vRot.x;

			float vTimeRot = TimeRot * ( -saturate( -v.vSize_vRot.y * 1000.0f ) + saturate( v.vSize_vRot.y * 1000.0f ) );
			float randSin = sin( v.vSize_vRot.y + vTimeRot );
			float randCos = cos( v.vSize_vRot.y + vTimeRot );

			vPos.xz = float2(
				vPos.x * randCos - vPos.z * randSin,
				vPos.x * randSin + vPos.z * randCos );

			//Semi-billboard
			//float3 Forward = cross( Right, Up );
			//vPos.y = dot( vPos, Forward ) * 0.3;

			//Real billboard
			//vPos.xyz = Right * vPos.x + Up * vPos.z;

			//Tilt
			vPos.y = ( v.vPosition.x + v.vPosition.y ) * v.vSize_vRot.x * 0.1f;

			vPos.xyz += v.vPos;

			float4 vPosition = mul( ViewProjectionMatrix, vPos );
			Out.vPos 		= vPos;
			Out.vPosition  	= vPosition;
			Out.vUV			= v.vUV;
			Out.vUVColor 	= ( vPos.xz + DustCloudUV.xy ) / DustCloudUV.zw;

			Out.vScreenCoord.x = ( Out.vPosition.x * 0.5 + Out.vPosition.w * 0.5 );
			Out.vScreenCoord.y = ( Out.vPosition.w * 0.5 - Out.vPosition.y * 0.5 );
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
			float4 vDiffuse = tex2D( DustTexture, v.vUV );

			float vTI = CalcTerraIncognitaValue( v.vPos.xz, TerraIncognitaTexture );

			float4 vColor = tex2D( ColorTexture, v.vUVColor );
			float4 vBorderColor = tex2Dproj( Border, v.vScreenCoord );

			vBorderColor.a = saturate( vBorderColor.a * 0.8f );
			vColor.rgb = lerp( vColor.rgb, vBorderColor.rgb, vBorderColor.a *1.9f );

			float vBorderTI = 0.80f; // Saturate border under TI
			vTI = saturate( vTI + ( vBorderColor.a * vBorderTI ) * saturate( ( 1.0f - vTI ) * 1000 ) );

			vColor = vDiffuse * lerp( vColor, vec4( TI_GRAY_BRIGHTNESS + vBorderColor.a * 0.3f  ), 1.0f - vTI );

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


Effect GalaxyDust
{
	VertexShader = "VertexShader";
	PixelShader = "PixelShader";
}
